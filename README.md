# rebuild-rpms

This repo contains recipes to rebuild RPMS that  are normally provided by the OS
and have corresponding SRPMS and spec files that can be resused with needed updates
and modifications.

## Individual packages info

### shadow-utils

   The original RPM provided by the OS (from baseOS repo) as of version 4.6
   enabled a call to `sss_cache` in most of the binaries such as useradd,
   usermod, etc. This call makes the execution of such binaries excessively slow
   as the SSSD cache is cleared. 

   To remedy, get the SRPM for the same version and reconfigure to disable use of SSSD,
   recompile and rebuild RPM. All needed files are in *shadow-utils/* of this repo.
   
   The source RPM was downloaded:

   ```bash
   wget https://download.rockylinux.org/pub/rocky/8/BaseOS/source/tree/Packages/s/shadow-utils-4.6-17.el8.src.rpm
   ```

   The spec file patch with needed changes was created by:

   ```bash
   diff -Naur shadow-utils.spec.orig shadow-utils.spec > spec-4.6-17.patch
   ```

   To build a new RPM using SRPM and spec patch file:


   1. Download this repo via:

      ```bash
      git clone git@github.com:RCIC-UCI-Public/rebuild-rpms.git
      ```

   1. Extract files from SRPM

      ```bash
      cd rebuild-rpms/shadow-utils
      mkdir builddir
      cd builddir
      rpm2cpio ../shadow-utils-4.6-17.el8.src.rpm | cpio -idmv
      ```

   1. Create directory structure for building RPMS:

      ```bash
      mkdir BUILD  RPMS  SOURCES  
      mv shadow-* gpl* SOURCES/
      cp SOURCES/shadow-utils.spec .
      ```

   1. Patch the spec file:

      In the patch, the changes include:

      * update source of 3 files to use those already available from SRPM
      * add info to description identifying package rebuild by `RCIC @ UC Irvine`
        and the reason for rebuild
      * update configiure command to disable SSSD
    
      ```bash
      patch -p0 < ../spec-4.6-17.patch
      ```

   1. Build RPMS:

      ```bash
      rpmbuild --define "_topdir `pwd`" -bb shadow-utils.spec 
      ```

      In case some prerequisite RPMS are missing on a build host the above command fails
      with errors specifying which RPMS are needed to be installed.  All required  RPMS
      are identified in spec file with `BuildRequires:` directives, and can be installed with yum,
      for example:

      ```bash
      yum install libsemanage-devel
      yum install itstool
      yum install audit-libs-devel
      yum install libacl-devel
      ```
      Rerun rpmobuild command. When successful, the resulting RPMS are in `RPMS/x86_64/`
      Copy RPMS to desired location and delete builddir:

      ```bash
      cd ../
      rm -rf builddir
      ```

      Resulting RPMS contain exactly the same subset of files as the original RPMs installed with the OS.
      To create RPMS in alternate locatino see the next step.

   1. Build RPMS for alternative location:

      In order to use an alternate location for the installed files need ot make a few additional
      changes to spec file.

      Copy `shadow-utils.spec` to a separate file and edit a copy as:

      * change RPM name to differentiate it from the original:

        ```
        Name: shadow-utils-no-sssd
        ```

      * in Globals section before any other line define _prefix and _sysconfdir for alternative installation location */opt/rcic*.
        All shadow-utils files will be configured and installed in respective  subdirectories under */opt/rcic*.

        ```
        ### Globals ###
        %define _prefix		/opt/rcic
        %define _sysconfdir	/opt/rcic/etc
        ```

      * in %files section (this is specifically for shadow-utils main RPM) add directives to include leading directories.
        This provides for clean removal of RPM.

        ```
        %dir %{_sysconfdir}
        %dir %{_bindir}
        %dir %{_sbindir}
        %dir %{_mandir}
        %dir %{_datadir}
        ```
      Save edited file as shadow-utils-alt.spec and build RPM as

      ```bash
      rpmbuild --define "_topdir `pwd`" -bb ../shadow-utils-alt.spec
      ```

