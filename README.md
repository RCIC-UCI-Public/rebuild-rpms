# rebuild-rpms

This repo contains recipes to rebuild RPMs that  are normally provided by the OS
and have corresponding SRPMs and spec files that are reused with needed updates
and modifications.

Individual recipes info by package.

## shadow-utils

The original RPM provided by the OS (from baseOS repo) as of version 4.6
enabled a call to `sss_cache` in most of the binaries such as `useradd,
usermod`, etc. This call makes the execution of such binaries excessively slow
as the SSSD cache is cleared. 

To remedy, get the SRPM for the same version and reconfigure to disable use of SSSD,
recompile and rebuild RPM. All needed files are in **shadow-utils/**  subdirectory of this repo.
   
This process needs to be run for each new version and release of the original shadow-utils
to keep the updated RPMs versions in sync with what system has.

Steps below are for shadow-utils version 4.6 release 22. Update version and release
accordingly when building for another version.

### Download source RPM

The source RPM was downloaded:

```bash
wget https://download.rockylinux.org/pub/rocky/8/BaseOS/source/tree/Packages/s/shadow-utils-4.6-22.el8.src.rpm
```

### Build a new RPM using SRPM and patched spec file

1. Download this repo via:

   ```bash
   git clone git@github.com:RCIC-UCI-Public/rebuild-rpms.git
   ```

1. Extract files from SRPM

   ```bash
   cd rebuild-rpms/shadow-utils
   mkdir builddir
   cd builddir
   rpm2cpio ../shadow-utils-4.6-22.el8.src.rpm | cpio -idmv
   ```

1. Create local directory structure needed for building RPMs:

   ```bash
   mkdir BUILD  RPMS  SOURCES  
   mv shadow-* gpl* SOURCES/
   cp SOURCES/shadow-utils.spec .
   ```

1. Create a spec patch file for a specific version/release:

   Save the original spec file 

   ```bash
   cp shadow-utils.spec shadow-utils.spec.orig
   ```

   Edit `shadow-utils.spec` file, the changes include:

   * update source of 3 files to use those already available from SRPM
   * add info to description identifying package rebuild by `RCIC @ UC Irvine`
     and the reason for rebuild
   * update configiure command to disable SSSD
   * change prefix, mandir, includedir, sysconfdir to `/opt/RCIC/shadow-utils/<version>`
   * changes the name of the RPMs from `shadow-utils` to `shadow-utils-no-sssd`
   * add prefix, mandir, includedir, sysconfigdir to %files for cleaner removal

   Create a patch file:

   ```bash
   diff -Naur shadow-utils.spec.orig shadow-utils.spec > ../spec-4.6-22.patch
   mv shadow-utils.spec.orig shadow-utils.spec
   ```
   The last ocmmand simply restores the file to its original so that we can apply
   a newly patch in the following step.

1. Patch the spec file:

   ```bash
   patch -p0 < ../spec-4.6-22.patch
   ```

1. Build RPMs:

  Use `rpmbuild` command to create RPM.

   In case some prerequisite system RPMs are missing on a build host the above command fails
   with errors specifying which RPMs are needed to be installed, for example:

   ```bash
   rpmbuild --define "_topdir `pwd`" -bb shadow-utils.spec 
   error: Failed build dependencies:
	/usr/bin/itstool is needed by shadow-utils-no-sssd-2:4.6-22.el8.x86_64
	audit-libs-devel >= 1.6.5 is needed by shadow-utils-no-sssd-2:4.6-22.el8.x86_64
	libacl-devel is needed by shadow-utils-no-sssd-2:4.6-22.el8.x86_64
	libattr-devel is needed by shadow-utils-no-sssd-2:4.6-22.el8.x86_64
	libsemanage-devel is needed by shadow-utils-no-sssd-2:4.6-22.el8.x86_64
   ```
   Install missing RPMs with yum:

   ```bash
   yum install itstool
   yum install audit-libs-devel
   yum install libacl-devel
   yum install libattr-devel
   yum install libsemanage-devel
   ```

   All required  RPMs are identified in spec file with `BuildRequires:` directives.
   Once missing RPMs are installed rerun `rpmbuild` command. 
   When successful, the resulting RPMs are in `RPMS/x86_64/`

   ```bash
   ls -1 RPMS/x86_64
   shadow-utils-no-sssd-4.6-22.el8.x86_64.rpm
   shadow-utils-no-sssd-subid-4.6-22.el8.x86_64.rpm 
   shadow-utils-no-sssd-subid-devel-4.6-22.el8.x86_64.rpm

   Copy RPMs to desired location and delete builddir:

   ```bash
   cd ../
   rm -rf builddir
   ```

   Resulting RPMs contain same subset of files as the original RPMs (minus build_id links) installed with the OS.
   BUT the install tree area has be been changed to /opt/RCIC/shadow-utils


### Build RPMs that *REPLACES* the system-supplied version

Follow the process above, EXCEPT use spec-sys-4.6-22.patch instead of spec-4.6-22.patch.  
     
You will probably have to edit the resulting spec file and bump the release from -22 to something
larger than the version supplied with the system -- this is so yum/dnf will pick the later version
of the rpm.

the "sys" spec file only does the following

* update source of 3 files to use those already available from SRPM
* add info to description identifying package rebuild by `RCIC @ UC Irvine`
  and the reason for rebuild
* update configiure command to disable SSSD

**NOTE: if you build this version, the OS-supplied version and this version cannot both be installed**.
