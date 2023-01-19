# rebuild-rpms

This repo contains recipes to rebuild RPMS that  are normally provided by the OS
and have correspons=nding SRPMS and spec files that can be resused with small updates
and modifications.

## Individual packages info

1. shadow-utils

   The original RPM provided by the OS (from baseOS repo) as of version 4.6
   has a call to `sss_cache` enabled in the most of the binaries such as 
   useradd, usermod, etc. The call makes execution of such binaries excessively slow
   as the SSSD cache is cleared. 

   To remedy, get the SRPM for the same version and reconfigure to disable this call,
   recompile and rebuild RPM. All needed files are in *shadow-utils/*
   
   The source RPM was downloaded and added to the repo:

   ```bash
   wget https://download.rockylinux.org/pub/rocky/8/BaseOS/source/tree/Packages/s/shadow-utils-4.6-17.el8.src.rpm
   ```

   The spec file patch with needed changes was created by:

   ```bash
   diff -Naur shadow-utils.spec.orig shadow-utils.spec > spec.patch
   ```

   To build a new RPM using SRPM and spec patch file:

   1. Install the following RPMs if missing, they are required for compiling from source:

      ```bash
      yum install libsemanage-devel
      yum install itstool
      yum install audit-libs-devel
      yum install libacl-devel
      ```

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
    
      ```bash
      patch -p0 < ../spec.patch 

      ```
   1. Build RPMS:

      ```bash
      rpmbuild --define "_topdir `pwd`" -bb shadow-utils.spec 
      ```

      Resulting RPMS are in `RPMS/x86_64/`
      Copy RPMS to desired location and delete builddir:

      ```bash
      cd ../
      rm -rf builddir
      ```

