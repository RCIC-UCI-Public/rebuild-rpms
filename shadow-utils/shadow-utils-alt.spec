Summary: Utilities for managing accounts and shadow password files
Name: shadow-utils-no-sssd
Version: 4.6
Release: 17%{?dist}
Epoch: 2
URL: http://pkg-shadow.alioth.debian.org/
Source0: shadow-%{version}.tar.xz
Source1: shadow-%{version}.tar.xz.asc
Source2: shadow-utils.useradd
Source3: shadow-utils.login.defs
Source4: shadow-bsd.txt
Source5: gpl-2.0.txt

### Globals ###
%define _prefix		/opt/rcic
%define _sysconfdir	/opt/rcic/etc
%global includesubiddir %{_includedir}/shadow 

### Patches ###
Patch0: shadow-4.6-redhat.patch
Patch1: shadow-4.6-goodname.patch
Patch2: shadow-4.1.5.1-info-parent-dir.patch
Patch6: shadow-4.6-selinux.patch
Patch10: shadow-4.6-orig-context.patch
Patch11: shadow-4.1.5.1-logmsg.patch
Patch14: shadow-4.1.5.1-default-range.patch
Patch15: shadow-4.6-manfix.patch
Patch17: shadow-4.1.5.1-userdel-helpfix.patch
Patch19: shadow-4.2.1-date-parsing.patch
Patch21: shadow-4.6-move-home.patch
Patch22: shadow-4.6-audit-update.patch
Patch23: shadow-4.5-usermod-unlock.patch
Patch24: shadow-4.2.1-no-lock-dos.patch
Patch28: shadow-4.3.1-selinux-perms.patch
Patch29: shadow-4.2.1-null-tm.patch
Patch31: shadow-4.6-getenforce.patch
Patch32: shadow-4.5-crypt_h.patch
Patch33: shadow-4.5-long-entry.patch
Patch34: shadow-4.6-usermod-crash.patch
Patch35: shadow-4.6-coverity.patch
Patch36: shadow-4.6-use-itstool.patch
Patch37: shadow-4.6-sssd-flush.patch
Patch38: shadow-4.6-sysugid-min-limit.patch
Patch39: shadow-4.6-chgrp-guard.patch
Patch40: shadow-4.6-ignore-login-prompt.patch
Patch41: shadow-4.6-use-lckpwdf.patch
# Upstreamed
Patch42: shadow-4.6-regular-user.patch
# Upstreamed
Patch43: shadow-4.6-home_mode-directive.patch
# Upstreamed
Patch44: shadow-4.6-check-local-groups.patch
# https://github.com/shadow-maint/shadow/commit/e84df9e163e133eb11a2728024ff3e3440592cf8
Patch45: shadow-4.6-sssd-redirect-warning.patch
# Unused option in Fedora/RHEL - non upstreamable
Patch46: shadow-4.6-remove-login-string-references.patch
# https://github.com/shadow-maint/shadow/commit/e481437ab9ebe9a8bf8fbaabe986d42b2f765991
Patch47: shadow-4.6-usermod-allow-all-group-types.patch
# https://github.com/shadow-maint/shadow/commit/0a7888b1fad613a052b988b01a71933b67296e68
# https://github.com/shadow-maint/shadow/commit/607f1dd549cf9abc87af1cf29275f0d2d11eea29
# https://github.com/shadow-maint/shadow/commit/b5fb1b38eea2fb0489ed088c82daf6700e72363e
# https://github.com/shadow-maint/shadow/commit/43a917cce54019799a8de037fd63780a2b640afc
Patch48: shadow-4.6-libsubid_creation.patch
# https://github.com/shadow-maint/shadow/commit/514c1328b6c90d817ae0a9f7addfb3c9a11a275a
# https://github.com/shadow-maint/shadow/commit/8492dee6632e340dee76eee895c3e30877bebf45
# https://github.com/shadow-maint/shadow/commit/0f4347d1483191b2142546416a9eefe0c9459600
Patch49: shadow-4.6-libsubid_nsswitch_support.patch
# https://github.com/shadow-maint/shadow/commit/186b1b7ac1a68d0fcc618a22da1a99232b420911
Patch50: shadow-4.6-man-mention-nss-in-newuidmap.patch
# https://github.com/shadow-maint/shadow/commit/f9831a4a1a20b0e8fe47cc72ec20018ec04dbb90
Patch51: shadow-4.6-libsubid_not_print_error_messages.patch
# https://github.com/shadow-maint/shadow/commit/c6cab4a7bafa18d9d65a333cac1261e7b5e32bc9
Patch52: shadow-4.6-libsubid_init_return_false.patch
# https://github.com/shadow-maint/shadow/commit/2f1f45d64fc7c10e7a3cbe00e89f63714343e526
Patch53: shadow-4.6-useradd_SUB_UID_COUNT-0.patch
# https://github.com/shadow-maint/shadow/commit/ea7af4e1543c63590d4107ae075fea385028997d
Patch54: shadow-4.6-libsubid_simplify_ranges_variable.patch
# https://github.com/shadow-maint/shadow/commit/0fe42f571c69f0105d31305f995c9887aeb9525e
Patch55: shadow-4.6-libsubid_init_not_print_error_messages.patch
# https://github.com/shadow-maint/shadow/commit/ec1951c181faed188464396b2cfdd2efb726c7f3
Patch56: shadow-4.6-libsubid_fix_newusers_nss_provides_subids.patch
# https://github.com/shadow-maint/shadow/commit/087112244327be50abc24f9ec8afbf60ae8b2dec
# https://github.com/shadow-maint/shadow/pull/353
Patch57: shadow-4.6-man_clarify_subid_delegation.patch
# https://github.com/shadow-maint/shadow/commit/bd920ab36a6c641e4a8769f8c7f8ca738ec61820
Patch58: shadow-4.6-libsubid_make_logfd_not_extern.patch
# https://github.com/shadow-maint/shadow/commit/0dffc7c61200f492eeac03c29fa7e93b62d3cead
Patch59: shadow-4.6-useradd_dont_try_to_create_0_subuids.patch
# https://github.com/shadow-maint/shadow/commit/77e39de1e6cbd6925f16bb260abb7d216296886b
Patch60: shadow-4.6-install_subid_h.patch
# https://github.com/shadow-maint/shadow/commit/fa986b1d73605ecca54a4f19249227aeab827bf6
Patch61: shadow-4.6-respect_enable_static_no.patch
# https://github.com/shadow-maint/shadow/commit/3b6ccf642c6bb2b7db087f09ee563ae9318af734
Patch62: shadow-4.6-getsubids.patch
# https://github.com/shadow-maint/shadow/commit/a757b458ffb4fb9a40bcbb4f7869449431c67f83
Patch63: shadow-4.6-groupdel-fix-sigsegv-when-passwd-does-not-exist.patch
# https://github.com/shadow-maint/shadow/commit/3ec32f9975f262073f8fbdecd2bfaee4a1d3db48
Patch64: shadow-4.9-subordinateio-compare-owner-ID.patch

License: BSD and GPLv2+
Group: System Environment/Base
BuildRequires: gcc
BuildRequires: libselinux-devel >= 1.25.2-1
BuildRequires: audit-libs-devel >= 1.6.5
BuildRequires: libsemanage-devel
BuildRequires: libacl-devel, libattr-devel
BuildRequires: bison, flex, docbook-style-xsl, docbook-dtds
BuildRequires: autoconf, automake, libtool, gettext-devel
BuildRequires: /usr/bin/xsltproc, /usr/bin/itstool
Requires: libselinux >= 1.25.2-1
Requires: audit-libs >= 1.6.5
Requires: setup
Requires(pre): coreutils
Requires(post): coreutils
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The shadow-utils package includes the necessary programs for
converting UNIX password files to the shadow password format, plus
programs for managing user and group accounts. The pwconv command
converts passwords to the shadow password format. The pwunconv command
unconverts shadow passwords and generates a passwd file (a standard
UNIX password file). The pwck command checks the integrity of password
and shadow files. The lastlog command prints out the last login times
for all users. The useradd, userdel, and usermod commands are used for
managing user accounts. The groupadd, groupdel, and groupmod commands
are used for managing group accounts.
This package is rebuilt from the original released SRPM by RCIC @ UC Irvine
The binaries in rebuilt package do not have calls to sss_cache.


### Subpackages ###
%package subid
Summary: A library to manage subordinate uid and gid ranges
License: BSD and GPLv2+

%description subid
Utility library that provides a way to manage subid ranges.


%package subid-devel
Summary: Development package for shadow-utils-subid
License: BSD and GPLv2+
Requires: shadow-utils-subid = %{epoch}:%{version}-%{release}

%description subid-devel
Development files for shadow-utils-subid.

%prep
%setup -q -n shadow-%{version}
%patch0 -p1 -b .redhat
%patch1 -p1 -b .goodname
%patch2 -p1 -b .info-parent-dir
%patch6 -p1 -b .selinux
%patch10 -p1 -b .orig-context
%patch11 -p1 -b .logmsg
%patch14 -p1 -b .default-range
%patch15 -p1 -b .manfix
%patch17 -p1 -b .userdel
%patch19 -p1 -b .date-parsing
%patch21 -p1 -b .move-home
%patch22 -p1 -b .audit-update
%patch23 -p1 -b .unlock
%patch24 -p1 -b .no-lock-dos
%patch28 -p1 -b .selinux-perms
%patch29 -p1 -b .null-tm
%patch31 -p1 -b .getenforce
%patch32 -p1 -b .crypt_h
%patch33 -p1 -b .long-entry
%patch34 -p1 -b .usermod-crash
%patch35 -p1 -b .coverity
%patch36 -p1 -b .use-itstool
%patch37 -p1 -b .sssd-flush
%patch38 -p1 -b .sysugid-min-limit
%patch39 -p1 -b .chgrp-guard
%patch40 -p1 -b .login-prompt
%patch41 -p1 -b .use-lckpwdf
%patch42 -p1 -b .regular-user
%patch43 -p1 -b .home_mode-directive
%patch44 -p1 -b .check-local-groups
%patch45 -p1 -b .sssd-redirect-warning
%patch46 -p1 -b .remove-login-string-references
%patch47 -p1 -b .usermod-allow-all-group-types
%patch48 -p1 -b .libsubid_creation
%patch49 -p1 -b .libsubid_nsswitch_support
%patch50 -p1 -b .man-mention-nss-in-newuidmap
%patch51 -p1 -b .libsubid_not_print_error_messages
%patch52 -p1 -b .libsubid_init_return_false
%patch53 -p1 -b .useradd_SUB_UID_COUNT-0
%patch54 -p1 -b .libsubid_simplify_ranges_variable
%patch55 -p1 -b .libsubid_init_not_print_error_messages
%patch56 -p1 -b .libsubid_fix_newusers_nss_provides_subids
%patch57 -p1 -b .man_clarify_subid_delegation
%patch58 -p1 -b .libsubid_make_logfd_not_extern
%patch59 -p1 -b .useradd_dont_try_to_create_0_subuids
%patch60 -p1 -b .install_subid_h
%patch61 -p1 -b .respect_enable_static_no
%patch62 -p1 -b .getsubids
%patch63 -p1 -b .groupdel-fix-sigsegv-when-passwd-does-not-exist
%patch64 -p1 -b .subordinateio-compare-owner-ID


iconv -f ISO88591 -t utf-8  doc/HOWTO > doc/HOWTO.utf8
cp -f doc/HOWTO.utf8 doc/HOWTO

cp -a %{SOURCE4} %{SOURCE5} .

# Force regeneration of getdate.c
rm libmisc/getdate.c

%build
%ifarch sparc64
#sparc64 need big PIE
export CFLAGS="$RPM_OPT_FLAGS -fPIE"
export LDFLAGS="-pie -Wl,-z,relro -Wl,-z,now"
%else
export CFLAGS="$RPM_OPT_FLAGS -fpie"
export LDFLAGS="-pie -Wl,-z,relro -Wl,-z,now"
%endif

autoreconf
%configure \
        --with-sssd=no \
        --enable-shadowgrp \
        --enable-man \
        --with-audit \
        --with-sha-crypt \
        --with-selinux \
        --without-libcrack \
        --without-libpam \
        --enable-shared \
        --with-group-name-max-length=32

%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install gnulocaledir=$RPM_BUILD_ROOT/%{_datadir}/locale MKINSTALLDIRS=`pwd`/mkinstalldirs
install -d -m 755 $RPM_BUILD_ROOT/%{_sysconfdir}/default
install -p -c -m 0644 %{SOURCE3} $RPM_BUILD_ROOT/%{_sysconfdir}/login.defs
install -p -c -m 0600 %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/default/useradd


ln -s useradd $RPM_BUILD_ROOT%{_sbindir}/adduser
ln -s useradd.8 $RPM_BUILD_ROOT/%{_mandir}/man8/adduser.8
for subdir in $RPM_BUILD_ROOT/%{_mandir}/{??,??_??,??_??.*}/man* ; do
        test -d $subdir && test -e $subdir/useradd.8 && echo ".so man8/useradd.8" > $subdir/adduser.8
done

# Remove binaries we don't use.
rm $RPM_BUILD_ROOT/%{_bindir}/chfn
rm $RPM_BUILD_ROOT/%{_bindir}/chsh
rm $RPM_BUILD_ROOT/%{_bindir}/expiry
rm $RPM_BUILD_ROOT/%{_bindir}/groups
rm $RPM_BUILD_ROOT/%{_bindir}/login
rm $RPM_BUILD_ROOT/%{_bindir}/passwd
rm $RPM_BUILD_ROOT/%{_bindir}/su
rm $RPM_BUILD_ROOT/%{_bindir}/faillog
rm $RPM_BUILD_ROOT/%{_sysconfdir}/login.access
rm $RPM_BUILD_ROOT/%{_sysconfdir}/limits
rm $RPM_BUILD_ROOT/%{_sbindir}/logoutd
rm $RPM_BUILD_ROOT/%{_sbindir}/nologin
rm $RPM_BUILD_ROOT/%{_mandir}/man1/chfn.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man1/chfn.*
rm $RPM_BUILD_ROOT/%{_mandir}/man1/chsh.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man1/chsh.*
rm $RPM_BUILD_ROOT/%{_mandir}/man1/expiry.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man1/expiry.*
rm $RPM_BUILD_ROOT/%{_mandir}/man1/groups.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man1/groups.*
rm $RPM_BUILD_ROOT/%{_mandir}/man1/login.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man1/login.*
rm $RPM_BUILD_ROOT/%{_mandir}/man1/passwd.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man1/passwd.*
rm $RPM_BUILD_ROOT/%{_mandir}/man1/su.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man1/su.*
rm $RPM_BUILD_ROOT/%{_mandir}/man5/limits.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man5/limits.*
rm $RPM_BUILD_ROOT/%{_mandir}/man5/login.access.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man5/login.access.*
rm $RPM_BUILD_ROOT/%{_mandir}/man5/passwd.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man5/passwd.*
rm $RPM_BUILD_ROOT/%{_mandir}/man5/porttime.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man5/porttime.*
rm $RPM_BUILD_ROOT/%{_mandir}/man5/suauth.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man5/suauth.*
rm $RPM_BUILD_ROOT/%{_mandir}/man8/logoutd.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man8/logoutd.*
rm $RPM_BUILD_ROOT/%{_mandir}/man8/nologin.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man8/nologin.*
rm $RPM_BUILD_ROOT/%{_mandir}/man3/getspnam.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man3/getspnam.*
rm $RPM_BUILD_ROOT/%{_mandir}/man5/faillog.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man5/faillog.*
rm $RPM_BUILD_ROOT/%{_mandir}/man8/faillog.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man8/faillog.*

find $RPM_BUILD_ROOT%{_mandir} -depth -type d -empty -delete
%find_lang shadow
for dir in $(ls -1d $RPM_BUILD_ROOT%{_mandir}/{??,??_??}) ; do
    dir=$(echo $dir | sed -e "s|^$RPM_BUILD_ROOT||")
    lang=$(basename $dir)
#   echo "%%lang($lang) $dir" >> shadow.lang
#   echo "%%lang($lang) $dir/man*" >> shadow.lang
    echo "%%lang($lang) $dir/man*/*" >> shadow.lang
done

# Move header files to its own folder
mkdir -p $RPM_BUILD_ROOT/%{includesubiddir}
install -m 644 libsubid/subid.h $RPM_BUILD_ROOT/%{includesubiddir}/

# Remove .la files created by libsubid
rm -f $RPM_BUILD_ROOT/%{_libdir}/libsubid.la

%files -f shadow.lang
%dir %{_sysconfdir}
%dir %{_bindir}
%dir %{_sbindir}
%dir %{_mandir}
%dir %{_datadir}
%doc NEWS doc/HOWTO README
%{!?_licensedir:%global license %%doc}
%license gpl-2.0.txt shadow-bsd.txt
%attr(0644,root,root)   %config(noreplace) %{_sysconfdir}/login.defs
%attr(0644,root,root)   %config(noreplace) %{_sysconfdir}/default/useradd
%{_bindir}/sg
%attr(4755,root,root) %{_bindir}/chage
%attr(4755,root,root) %{_bindir}/gpasswd
%{_bindir}/lastlog
%attr(4755,root,root) %{_bindir}/newgrp
%attr(0755,root,root) %caps(cap_setgid=ep) %{_bindir}/newgidmap
%attr(0755,root,root) %caps(cap_setuid=ep) %{_bindir}/newuidmap
%{_sbindir}/adduser
%attr(0755,root,root)   %{_sbindir}/user*
%attr(0755,root,root)   %{_sbindir}/group*
%{_sbindir}/grpck
%{_sbindir}/pwck
%{_sbindir}/*conv
%{_sbindir}/chpasswd
%{_sbindir}/chgpasswd
%{_sbindir}/newusers
%{_sbindir}/vipw
%{_sbindir}/vigr
%{_mandir}/man1/chage.1*
%{_mandir}/man1/gpasswd.1*
%{_mandir}/man1/sg.1*
%{_mandir}/man1/newgrp.1*
%{_mandir}/man1/newgidmap.1*
%{_mandir}/man1/newuidmap.1*
%{_mandir}/man3/shadow.3*
%{_mandir}/man5/shadow.5*
%{_mandir}/man5/login.defs.5*
%{_mandir}/man5/gshadow.5*
%{_mandir}/man5/subuid.5*
%{_mandir}/man5/subgid.5*
%{_mandir}/man8/adduser.8*
%{_mandir}/man8/group*.8*
%{_mandir}/man8/user*.8*
%{_mandir}/man8/pwck.8*
%{_mandir}/man8/grpck.8*
%{_mandir}/man8/chpasswd.8*
%{_mandir}/man8/chgpasswd.8*
%{_mandir}/man8/newusers.8*
%{_mandir}/man8/*conv.8*
%{_mandir}/man8/lastlog.8*
%{_mandir}/man8/vipw.8*
%{_mandir}/man8/vigr.8*

%files subid
%{_libdir}/libsubid.so.*
%{_bindir}/getsubids
%{_mandir}/man1/getsubids.1*

%files subid-devel
%{includesubiddir}/subid.h
%{_libdir}/libsubid.so

%changelog
* Thu Jul 21 2022 Iker Pedrosa <ipedrosa@redhat.com> - 2:4.6-17
- subordinateio: also compare the owner ID. Resolves: #2093311
- Fix release sources
- Add subid requirement for subid-devel

* Thu Dec  9 2021 Iker Pedrosa <ipedrosa@redhat.com> - 2:4.6-16
- getsubids: provide system binary and man page. Resolves: #2013016
- groupdel: fix SIGSEGV when passwd does not exist. Resolves: #1986782

* Tue Oct 19 2021 Iker Pedrosa <ipedrosa@redhat.com> - 2:4.6-15
- Creation of subid and subid-devel subpackages (#2013009)
- libsubid: creation and nsswitch support
- libsubid: don't print error messages on stderr by default
- libsubid: libsubid_init return false if out of memory
- libsubid: don't return owner in list_owner_ranges API call
- libsubid: libsubid_init don't print messages on error
- libsubid: fix newusers when nss provides subids
- libsubid: make shadow_logfd not extern
- useradd: fix SUB_UID_COUNT=0
- man: mention NSS in new[ug]idmap manpages
- man: clarify subid delegation

* Thu Aug 12 2021 Iker Pedrosa <ipedrosa@redhat.com> - 2:4.6-14
- usermod: allow all group types with -G option (#1967641)

* Mon May  3 2021 Iker Pedrosa <ipedrosa@redhat.com> - 2:4.6-13
- man: Remove references to LOGIN_STRING in login.defs (#1884702)

* Fri Oct 23 2020 Iker Pedrosa <ipedrosa@redhat.com> - 2:4.6-12
- lib/sssd: redirect warning message to file (#1749001)
- useradd: clarify valid usernames/groupnames (#1869432)
- login.defs: link login specific information to its own package (#1804766)

* Fri Aug  7 2020 Iker Pedrosa <ipedrosa@redhat.com> - 2:4.6-11
- change UMASK value and add HOME_MODE in login.defs (#1777718)

* Tue May  5 2020 Iker Pedrosa <ipedrosa@redhat.com> - 2:4.6-10
- check only local groups when adding new supplementary groups to a user

* Fri Apr 17 2020 Iker Pedrosa <ipedrosa@redhat.com> - 2:4.6-9
- do not mistake a regular user process for a namespaced one (#1788696)
- add HOME_MODE support in login.defs (#1777718)

* Fri Jun  7 2019 Tomáš Mráz <tmraz@redhat.com> - 2:4.6-8
- properly audit group password change
- do not add uid of a new (not yet added) user to the audit message
- use lckpwdf() again to disable concurrent edits of databases by
  other applications
- clarify chage manual page in regards to shadow and passwd
  inconsistency
- fix minor issues in groupadd and login.defs manual pages
- Ignore LOGIN_PLAIN_PROMPT variable in login.defs
- force regeneration of getdate.c otherwise the date parsing fix
  is not applied

* Tue Dec 18 2018 Tomáš Mráz <tmraz@redhat.com> - 2:4.6-7
- usermod: guard against unsafe change of ownership of
  special home directories

* Fri Nov 30 2018 Tomáš Mráz <tmraz@redhat.com> - 2:4.6-6
- drop trailing space from login.defs ENCRYPT_METHOD setting

* Mon Nov 19 2018 Tomáš Mráz <tmraz@redhat.com> - 2:4.6-5
- use cap_setxid file capabilities for newxidmap instead of making them setuid
- limit the SYS_U/GID_MIN value to 1 as the algorithm does not work with 0
  and the 0 is always used by root anyway
- manual page improvements
- flush sssd caches - patch by Jakub Hrozek

* Fri Oct 12 2018 Tomáš Mráz <tmraz@redhat.com> - 2:4.6-4
- fix some issues from Coverity scan

* Tue Jul 31 2018 Tomáš Mráz <tmraz@redhat.com> - 2:4.6-2
- use itstool instead of xml2po

* Tue Jul 31 2018 Tomáš Mráz <tmraz@redhat.com> - 2:4.6-1
- Update to current upstream release 4.6
- Raise limit for passwd and shadow entry length but also prevent
  writing longer entries (#1422497)

* Tue Feb 06 2018 Björn Esser <besser82@fedoraproject.org> - 2:4.5-9
- Add patch to include crypt.h, if present
- Use %%make_{build,install} macros
- Refresh other patches for proper alignment

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2:4.5-8
- Rebuilt for switch to libxcrypt

* Mon Nov  6 2017 Tomáš Mráz <tmraz@redhat.com> - 2:4.5-7
- fix regression caused by the userdel-chroot patch (#1509978)

* Thu Nov  2 2017 Tomáš Mráz <tmraz@redhat.com> - 2:4.5-6
- fix userdel in chroot (#1316168)
- add useful chage -E example to chage manpage

* Fri Sep 15 2017 Tomáš Mráz <tmraz@redhat.com> - 2:4.5-5
- do not allow "." and ".." user names

* Mon Aug 14 2017 Tomáš Mráz <tmraz@redhat.com> - 2:4.5-4
- allow switching to secondary group without checking the membership
  explicitly (patch from upstream)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Tomáš Mráz <tmraz@redhat.com> - 2:4.5-1
- update to current upstream release 4.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 25 2016 Tomáš Mráz <tmraz@redhat.com> - 2:4.3.1-2
- fix regression in useradd - not processing defaults properly (#1369979)

* Tue Aug 23 2016 Tomáš Mráz <tmraz@redhat.com> - 2:4.3.1-1
- new upstream release fixing low impact security issue

* Tue Jun 14 2016 Tomáš Mráz <tmraz@redhat.com> - 2:4.2.1-11
- guard for localtime() and gmtime() failure

* Mon May 30 2016 Tomáš Mráz <tmraz@redhat.com> - 2:4.2.1-10
- chpasswd, chgpasswd: open audit when starting

* Thu May 26 2016 Tomáš Mráz <tmraz@redhat.com> - 2:4.2.1-9
- chgpasswd: do not remove it
- chpasswd, chgpasswd: add selinux_check_access call (#1336902)

* Thu Mar 17 2016 Tomáš Mráz <tmraz@redhat.com> - 2:4.2.1-8
- userdel: fix userdel -f with /etc/subuid present (#1316168)

* Tue Feb  9 2016 Tomáš Mráz <tmraz@redhat.com> - 2:4.2.1-7
- usermod: properly return error during password manipulation

* Wed Feb  3 2016 Tomáš Mráz <tmraz@redhat.com> - 2:4.2.1-6
- add possibility to clear or set lastlog record for user via lastlog

* Fri Jan  8 2016 Tomáš Mráz <tmraz@redhat.com> - 2:4.2.1-5
- do not use obscure permissions for binaries
- remove unused commands from login.defs(5) cross-reference

* Fri Nov  6 2015 Tomáš Mráz <tmraz@redhat.com> - 2:4.2.1-4
- document that groupmems is not setuid root
- document that expiration of the password after inactivity period
  locks the user account completely

* Thu Aug 27 2015 Tomáš Mráz <tmraz@redhat.com> - 2:4.2.1-3
- unlock also passwords locked with passwd -l
- prevent breaking user entry by entering a password containing colon
- fix possible DoS when locking the database files for update
- properly use login.defs from the chroot in useradd

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 26 2014 Tomáš Mráz <tmraz@redhat.com> - 2:4.2.1-1
- new upstream release with support for subordinate uids and gids

* Tue Nov 25 2014 Tomáš Mráz <tmraz@redhat.com> - 2:4.1.5.1-22
- small adjustments to the audit patch

* Fri Oct 17 2014 Tomáš Mráz <tmraz@redhat.com> - 2:4.1.5.1-21
- update auditing to cover more events and fix some incorrect audit
  records - patch by Steve Grubb (#1151580)
- apply the same new allocation algorithm to uids as for gids

* Wed Sep 10 2014 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-20
- discard obsolete matchpathcon cache after semanage_commit()

* Tue Sep  9 2014 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-19
- disallow all-numeric user and group names (#1139318)

* Fri Aug 29 2014 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-18
- label the newly created home dir correctly (#1077809)
- mention that chage -d 0 forces password change (#1135010)
- improve date parsing and error detecting in chage
- avoid full group database scanning in newgrp in most common case
- report error if usermod asked for moving homedir and it does not exist

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:4.1.5.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug  5 2014 Tom Callaway <spot@fedoraproject.org> - 2:4.1.5.1-16
- fix license handling

* Mon Jul 14 2014 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-15
- revert the last change as it is not really needed

* Thu Jul 10 2014 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-14
- put system users and groups into /usr/lib/{passwd,group} if
  the files exist and SHADOW_USE_USRLIB environment variable is set
  Patch by Colin Walters

* Mon Jun 30 2014 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-13
- ignore getgrgid() errors for now

* Mon Jun 30 2014 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-12
- improve group allocation algorithm - patch by Stephen Gallager (#1089738)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:4.1.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-10
- clean up login.defs manpage
- properly document userdel -f behavior

* Fri Oct 18 2013 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-9
- document that the directory where user's home is created must exist

* Thu Jul 25 2013 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-8
- slightly more meaningful error messages if crypt() returns NULL (#988184)
- explicit suid permissions

* Fri Jul 19 2013 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-7
- fix useradd man page bugs

* Fri Jun 14 2013 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-6
- report error to stdout when SELinux context for home directory
  cannot be determined (#973647)
- audit the changing home directory owner (#885797)
- do not set the default SELinux MLS range (#852676)

* Tue Mar 19 2013 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-5
- improve the failure syslog message in useradd (#830617)

* Wed Feb 20 2013 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-4
- keep the original context if matchpathcon() fails (#912399)

* Tue Jan 29 2013 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-3
- fix bugs in merge_group_entries()

* Fri Jan 11 2013 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-2
- /etc/default is owned by glibc-common now (#894194)

* Wed Sep 19 2012 Tomas Mraz <tmraz@redhat.com> - 2:4.1.5.1-1
- new upstream version
- use the original file permissions when creating backup (#853102)

* Wed Jul 25 2012 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.5-5
- make /etc/default/useradd world-readable (#835137)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:4.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 18 2012 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.5-3
- pwconv/grpconv skipped 2nd of consecutive failures (#832995)

* Thu Mar 22 2012 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.5-2
- fix selinux context handling
- reset selinux context on files copied from skel

* Mon Mar 19 2012 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.5-1
- upgrade

* Tue Feb 07 2012 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.3-14
- compile with PIE and RELRO flags (#784349)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:4.1.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.3-12
- fix leaks in .IDs patch (#734340)

* Wed Nov 16 2011 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.3-11
- free memory associated with SELinux security contexts

* Wed Nov 09 2011 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.3-10
- replace semanage call by library call
- useradd man page (#739147)

* Tue Aug 02 2011 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.3-9
- man page adjustment (userdel -Z)

* Tue Aug 02 2011 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.3-8
- fixing semanage issue (#701355)

* Fri Jul 22 2011 Miloslav Trmač <mitr@redhat.com> - 2:4.1.4.3-7
- Make sure /etc/login.defs is not changed on upgrades from Fedora 1[345].

* Wed Jun 29 2011 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.3-6
- man page fixes (#696213 #674878)

* Tue Jun 28 2011 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.3-5
- userdel option to remove Linux login <-> SELinux login mapping (#639900)
- useradd special exit value if SELinux user mapping is invalid (#639975)
- usermod special exit value if SELinux user mapping is invalid (#639976)

* Mon Jun 27 2011 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.3-4
- refer to PAM in /etc/login.defs (#629277)

* Mon Jun 06 2011 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.3-3
- fix shadow-4.1.4.2-underflow.patch

* Tue May 31 2011 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.3-2
- fix integer underflow in laslog (#706321)

* Fri May 20 2011 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.3-1
- upgrade
- change UID/GID_MIN to #1000
- fix find_new_uid/gid for big UID/GID_MAX

* Wed Feb 09 2011 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.2-11
- useradd man page (-m option)
- create home directory on fs with noacl
- remove faillog app (pam_tally.so is no longer shipped)
  Resolves: #523265, #622320

* Tue Feb 01 2011 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.2-10
- do not use  gshadow functions from glibc, there is a bug
  in glibc sgetsgent(#674361)
  Resolves: #674234

* Wed Jan 05 2011 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.2-9
- fix gshadow functions from shadow utils
- make shadow utils use gshadow functions from glibc
  Resolves: #665780

* Tue Jul 20 2010 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.2-8
- fix pwck/grpck hang
  Resolves: #586322

* Mon Jun 14 2010 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.2-7
- fix integer underflow in faillog (#603683)
- use preferred GID for reserved static IDs

* Thu Apr 29 2010 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.2-6
- preserve ACL's on files in /etc/skel
  Resolves: #513055

* Wed Apr 28 2010 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.2-5
- newusers man page more informative
- userdel should not need to run semanage
  Resolves: #586330 #586408

* Thu Apr 01 2010 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.2-4
- fix man directories ownership (#569418)

* Fri Mar 26 2010 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.2-3
- max group name length set to 32 characters

* Wed Nov 18 2009 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.2-2
- apply patches{1,2,3}
- enable SHA512 in /etc/login.defs

* Mon Sep 07 2009 Peter Vrabec <pvrabec@redhat.com> - 2:4.1.4.2-1
- upgrade

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2:4.1.4.1-7
- rebuilt with new audit

* Wed Aug 05 2009 Peter Vrabec <pvrabec@redhat.com> 2:4.1.4.1-6
- increase threshold for uid/gid reservations to 200 (#515667)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:4.1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Peter Vrabec <pvrabec@redhat.com> 2:4.1.4.1-4
- fix a list of owned directories (#510366)

* Thu Jul 16 2009 Peter Vrabec <pvrabec@redhat.com> 2:4.1.4.1-3
- reduce the reuse of system IDs

* Wed Jul 15 2009 Peter Vrabec <pvrabec@redhat.com> 2:4.1.4.1-2
- speed up sys users look up on LDAP boxes (#511813)

* Tue Jun 16 2009 Peter Vrabec <pvrabec@redhat.com> 2:4.1.4.1-1
- upgrade

* Fri May 15 2009 Peter Vrabec <pvrabec@redhat.com> 2:4.1.4-1
- upgrade

* Wed Apr 22 2009 Peter Vrabec <pvrabec@redhat.com> 2:4.1.3.1-2
- lastlog fix

* Fri Apr 17 2009 Peter Vrabec <pvrabec@redhat.com> 2:4.1.3.1-1
- upgrade

* Tue Apr 14 2009 Peter Vrabec <pvrabec@redhat.com> 2:4.1.3-2
- get "-n" option back
- fix selinux issues

* Tue Apr 14 2009 Peter Vrabec <pvrabec@redhat.com> 2:4.1.3-1
- upgrade

* Tue Mar 24 2009 Peter Vrabec <pvrabec@redhat.com> 2:4.1.2-12
- don not allow UID/GID = 4294967295 (#484040)

* Mon Jan 19 2009 Peter Vrabec <pvrabec@redhat.com> 2:4.1.2-11
- fix license tag (#226416)
- get rid of tabs in spec file (#226416)
- convert HOWTO to UTF8 (#226416)

* Mon Jan 05 2009 Peter Vrabec <pvrabec@redhat.com> 2:4.1.2-10
- Add policycoreutils as Requires, because of restorecon (#478494)

* Sun Dec 21 2008 Jesse Keating <jkeating@redhat.com> - 2:4.1.2-9
- Add setup as a Requires. Perhaps this should be a files requires. (#477529)

* Wed Sep 24 2008 Peter Vrabec <pvrabec@redhat.com> 2:4.1.2-8
- groupmems: check username for valid character (#455603)
- groupmems: don't segfault on nonexistent group (#456088)

* Thu Sep 11 2008 Peter Vrabec <pvrabec@redhat.com> 2:4.1.2-7
- fix usermod SELinux user mappings change (#458766)

* Tue Sep 02 2008 Peter Vrabec <pvrabec@redhat.com> 2:4.1.2-6
- audit improvements, thnx. to sgrubb@redhat.com

* Tue Sep 02 2008 Peter Vrabec <pvrabec@redhat.com> 2:4.1.2-5
- fix groupmems issues (#459825)

* Mon Jul 28 2008 Peter Vrabec <pvrabec@redhat.com> 2:4.1.2-4
- fix configure options (#456748)

* Thu Jul 24 2008 Peter Vrabec <pvrabec@redhat.com> 2:4.1.2-3
- recreate selinux patch

* Tue Jul 22 2008 Peter Vrabec <pvrabec@redhat.com> 2:4.1.2-2
- provide getspnam by man-pages

* Mon May 26 2008 Peter Vrabec <pvrabec@redhat.com> 2:4.1.2-1
- upgrade

* Tue May 20 2008 Peter Vrabec <pvrabec@redhat.com> 2:4.1.1-2
- fix salt size problem (#447136)

* Mon Apr 07 2008 Peter Vrabec <pvrabec@redhat.com> 2:4.1.1-1
- upgrade

* Fri Mar 07 2008 Peter Vrabec <pvrabec@redhat.com> 2:4.1.0-5
- improve newgrp audit patch

* Mon Mar 03 2008 Peter Vrabec <pvrabec@redhat.com> 2:4.1.0-4
- fix selinux labeling  (#433757)

* Tue Feb 19 2008 Peter Vrabec <pvrabec@redhat.com> 2:4.1.0-3
- fix groupmems segmentation fault (#430813)

* Wed Feb 13 2008 Peter Vrabec <pvrabec@redhat.com> 2:4.1.0-2
- fix newgrp audit event

* Wed Dec 12 2007 Peter Vrabec <pvrabec@redhat.com> 2:4.1.0-1
- new upgrade release from new upstream
- provide vipw and vigr

* Thu Nov 29 2007 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-20
- do not create mail spool entries for system accounts (#402351)

* Thu Oct 18 2007 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-19
- fix timestamps when moving home dirs to another file system (#278571)

* Mon Oct 08 2007 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-18
- mark localized man pages with %%lang

* Wed Aug 22 2007 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-17
- rebuild

* Tue Jun 26 2007 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-16
- fix "CAVEATS" section of groupadd man page (#245590)

* Wed Jun 06 2007 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-15
- fix infinitive loop if there are duplicate entries
  in /etc/group (#240915)

* Wed Jun 06 2007 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-14
- do not run find_new_uid() twice and use getpwuid() to check
  UID uniqueness (#236871)

* Tue Apr 10 2007 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-13
- fix useradd dump core when build without WITH_SELINUX (#235641)

* Mon Mar 26 2007 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-12
- create user's mailbox file by default (#231311)

* Fri Mar 16 2007 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-11
- assign system dynamic UID/GID from the top of available UID/GID (#190523)

* Wed Feb 28 2007 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-10
- spec file fixes to meet fedora standarts.
- fix useless call of restorecon(). (#222159)

* Sun Jan 14 2007 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-9
- fix append option in usermod (#222540).

* Thu Dec 21 2006 Dan Walsh <dwalsh@redhat.com> 2:4.0.18.1-8
- Fix execution and creation of Home Directories under SELinux
- Resolves: rhbz#217441

* Thu Dec 14 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-7
- fix rpmlint issues

* Wed Dec 06 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-6
- use MD5 encryption by default (#218629).

* Thu Nov 30 2006 Steve Grubb <sgrubb@redhat.com> 2:4.0.18.1-5
- Fix SELinux context on home directories created with useradd (#217441)

* Tue Nov 14 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-4
- fix chpasswd and chgpasswd stack overflow (#213052)

* Sat Nov 04 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-3
- fix "-g" and "-G" option.

* Fri Nov 03 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-2
- improve audit logging (#211659)
- improve "-l" option. Do not reset faillog if it's used (#213450).

* Wed Nov 01 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.18.1-1
- upgrade

* Wed Oct 25 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.17-7
- add dist-tag

* Wed Oct 04 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.17-6
- fix regression. Permissions on user* group* binaries
  should be 0750, because of CAPP/LSPP certification
- fix groupdel man page

* Fri Aug 11 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.17-5
- fix bug introduced with UIG_GID.patch (#201991)

* Sat Aug 05 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.17-4
- fix userdel, it didn't delete user's group (#201379)

* Fri Aug 04 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.17-3
- fix UID/GID overflow in user* group* (#198920)

* Fri Aug 04 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.17-2
- do not inherit file desc. in execve(nscd)

* Mon Jul 17 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.17-1
- upgrade

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2:4.0.16-3.1
- rebuild

* Tue Jun 13 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.16-3
- call "nscd -i" to flush nscd cache (#191464)

* Sat Jun 10 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.16-2
- "useradd -r" must create a system group (#194728)

* Tue Jun 06 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.16-1
- upgrade
- do not replace login.defs file (#190014)

* Sat Apr 08 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.15-3
- fix typo in shadow-4.0.15-login.defs (#188263)

* Tue Apr 04 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.15-2
- properly notify nscd to flush its cache(#186803)

* Mon Apr 03 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.15-1
- upgrade

* Fri Mar 10 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.14-4
- fix lrename() function to handle relative symlinks too

* Tue Mar 07 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.14-3
- set default umask to 077 in login.defs

* Mon Mar 06 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.14-2
- use lrename() function, which follow a destination symbolic link(#181977)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2:4.0.14-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2:4.0.14-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 06 2006 Peter Vrabec <pvrabec@redhat.com> 2:4.0.14-1
- upgrade

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Nov 29 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.13-4
- fix incorrect audit record in userdel (#174392)

* Wed Nov 16 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.13-3
- fix useradd segfaults (#173241)

* Sat Nov 5 2005 Steve Grubb <sgrubb@redhat.com> 2:4.0.13-2
- Update audit communication to standard format messages

* Fri Oct 21 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.13-1
- upgrade

* Fri Sep 23 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.12-4
- add useradd -l option back, it was removed by mistake

* Tue Sep 20 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.12-3
- provide login.defs man page
- adjust audit patch

* Tue Aug 30 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.12-2
- audit support

* Sat Aug 27 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.12-1
- upgrade

* Sat Aug 13 2005 Dan Walsh <dwalsh@redhat.com> 2:4.0.11.1-5
- Change to use new selinux api for selinux_check_passwd_access

* Tue Aug 09 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.11.1-4
- change the password last changed field in the shadow file
  when "usermod -p" is used (#164943)

* Mon Aug 08 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.11.1-3
- provide getspnam.3 man page(#162476)
- fix useradd man page(#97131)

* Mon Aug 08 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.11.1-2
- do not copy files from skel directory if home directory
  already exist (#89591,#80242)

* Fri Aug 05 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.11.1-1
- upgrade

* Mon May 23 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.7-9
- remove vigr binary

* Mon May 23 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.7-8
- fix nscd socket path

* Fri Apr 29 2005 Jeremy Katz <katzj@redhat.com> - 2:4.0.7-7
- don't assume selinux is enabled if is_selinux_enabled() returns -1

* Mon Apr 18 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.7-6
- fix chage -l option (#109499, #137498)

* Mon Apr 04 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.7-5
- fix memory leak, and CPU spinning when grp_update() and
  duplicate group entries in /etc/group (#151484)

* Tue Mar 29 2005 Peter Vrabec <pvrabec@redhat.com>  2:4.0.7-4
- use newgrp binary
- newgrp don't ask for password if user's default GID = group ID,
  ask for password if there is some in /etc/gshadow
  and in /etc/group is 'x' (#149997)

* Mon Mar 14 2005 Peter Vrabec <pvrabec@redhat.com>
- gcc4 fix (#150994) 2:4.0.7-3

* Mon Mar 07 2005 Peter Vrabec <pvrabec@redhat.com>
- man pages cs,es,ko,ru,zh_CN,zh_TW to UTF-8

* Wed Mar 02 2005 Peter Vrabec <pvrabec@redhat.com>
- upgrade 2:4.0.7-1

* Fri Feb 25 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.3-59
- static limit on group count to dynamic (#125510, #148994, #147742)

* Mon Feb 21 2005 Peter Vrabec <pvrabec@redhat.com> 2:4.0.3-58
- add "-l" option #146214

* Mon Feb 14 2005 Adrian Havill <havill@redhat.com>
- rebuilt

* Wed Feb 9 2005 Dan Walsh <dwalsh@redhat.com> 2:4.0.3-39
- Change useradd to use matchpathcon

* Thu Oct 21 2004 Dan Walsh <dwalsh@redhat.com> 2:4.0.3-37
- Add matchpathcon to create the files correctly when they do not exist.

* Mon Oct 18 2004 Miloslav Trmac <mitr@redhat.com> - 2:4.0.3-36
- Change symlink ownership when copying from /etc/skel (#66819, patch by
  Michael Weiser)

* Fri Oct 15 2004 Adrian Havill <havill@redhat.com> 2:4.0.3-35
- make the limit for the group name the same as the username (determined
  by the header files, rather than a constant) (#56850)

* Wed Oct 13 2004 Adrian Havill <havill@redhat.com> 2:4.0.3-33
- allow for mixed case and dots in usernames (#135401)
- all man pages to UTF-8, not just Japanese (#133883)
- add Polish blurb for useradd -n man page option (#82177)

* Tue Oct 12 2004 Adrian Havill <havill@redhat.com> 2:4.0.3-31
- check for non-standard legacy place for ncsd HUP (/var/run/nscd.pid) and
  then the std FHS place (/var/run/nscd.pid) (#125421)

* Fri Oct 1 2004 Dan Walsh <dwalsh@redhat.com> 2:4.0.3-30
- Add checkPasswdAccess for chage in SELinux

* Sun Sep 26 2004 Adrian Havill <riel@redhat.com> 2:4.0.3-29
- always unlock all files on any exit (#126709)

* Tue Aug 24 2004 Warren Togami <wtogami@redhat.com> 2:4.0.3-26
- #126596 fix Req and BuildReqs

* Sun Aug  1 2004 Alan Cox <alan@redhat.com> 4.0.3-25
- Fix build deps etc, move to current auto* (Steve Grubb)

* Sat Jul 10 2004 Alan Cox <alan@redhat.com> 4.0.3-24
- Fix nscd path. This fixes various stale data caching bugs (#125421)

* Thu Jun 17 2004 Dan Walsh <dwalsh@redhat.com> 4.0.3-23
- Add get_enforce checks
- Clean up patch for potential upstream submission
- Add removemalloc patch to get it to build on 3.4

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 30 2004 Nalin Dahyabhai <nalin@redhat.com> 4.0.3-21
- rebuild

* Tue Mar 30 2004 Nalin Dahyabhai <nalin@redhat.com> 4.0.3-20
- make /etc/default world-readable, needed for #118338

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 21 2004 Dan Walsh <dwalsh@redhat.com> 4.0.3-18
- Fix selinux relabel of /etc/passwd file

* Wed Jan  7 2004 Nalin Dahyabhai <nalin@redhat.com> 4.0.3-17
- fix use of uninitialized memory in useradd (#89145)

* Tue Dec 16 2003 Nalin Dahyabhai <nalin@redhat.com> 4.0.3-16
- back to UTF-8 again
- remove getspnam(3) man page, now conflicts with man-pages 1.64

* Thu Nov 13 2003 Nalin Dahyabhai <nalin@redhat.com> 4.0.3-15
- don't convert man pages to UTF-8 for RHEL 3, conditionalized using macro
- fixup dangling man page references

* Mon Nov 10 2003 Nalin Dahyabhai <nalin@redhat.com> 4.0.3-14
- lastlog: don't pass a possibly-smaller field to localtime (#109648)
- configure: call AC_SYS_LARGEFILE to get large file support

* Fri Nov 7 2003 Dan Walsh <dwalsh@redhat.com> 4.0.3-13.sel
- turn on SELinux support

* Wed Oct 22 2003 Nalin Dahyabhai <nalin@redhat.com> 4.0.3-12
- convert ja man pages to UTF-8 (#106051)
- override MKINSTALLDIRS at install-time (#107476)

* Mon Sep 8 2003 Dan Walsh <dwalsh@redhat.com>
- turn off SELinux support

* Thu Sep 4 2003 Dan Walsh <dwalsh@redhat.com> 4.0.3-11.sel
- build with SELinux support

* Mon Jul 28 2003 Dan Walsh <dwalsh@redhat.com> 4.0.3-10
- Add SELinux support

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun  4 2003 Nalin Dahyabhai <nalin@redhat.com> 4.0.3-8
- rebuild

* Tue Jun  3 2003 Nalin Dahyabhai <nalin@redhat.com> 4.0.3-7
- run autoconf to generate updated configure at compile-time

* Wed Feb 12 2003 Nalin Dahyabhai <nalin@redhat.com> 4.0.3-6
- adjust mailspool patch to complain if no group named "mail" exists, even
  though that should never happen

* Tue Feb 11 2003 Nalin Dahyabhai <nalin@redhat.com> 4.0.3-5
- fix perms on mailspools created by useradd to be owned by the "mail"
  group (#59810)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec  9 2002 Nalin Dahyabhai <nalin@redhat.com> 4.0.3-3
- install the shadow.3 man page

* Mon Nov 25 2002 Nalin Dahyabhai <nalin@redhat.com> 4.0.3-2
- disable use of cracklib at build-time
- fixup reserved-account changes for useradd

* Thu Nov 21 2002 Nalin Dahyabhai <nalin@redhat.com> 4.0.3-1
- update to 4.0.3, bumping epoch

* Mon Nov 18 2002 Nalin Dahyabhai <nalin@redhat.com> 20000902-14
- remove man pages which conflict with the man-pages package(s)

* Fri Nov 15 2002 Nalin Dahyabhai <nalin@redhat.com> 20000902-13
- prevent libshadow from being built more than once, to keep automake happy
- change how md5 and md5crypt are enabled, to keep autoconf happy
- remove unpackaged files after %%install

* Thu Aug 29 2002 Nalin Dahyabhai <nalin@redhat.com> 20000902-12
- force .mo files to be regenerated with current gettext to flush out possible
  problems
- fixup non-portable encodings in translations
- make sv translation header non-fuzzy so that it will be included (#71281)

* Fri Aug 23 2002 Nalin Dahyabhai <nalin@redhat.com> 20000902-11
- don't apply aging parameters when creating system accounts (#67408)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri May 17 2002 Nalin Dahyabhai <nalin@redhat.com> 20000902-8
- rebuild in new environment

* Wed Mar 27 2002 Nalin Dahyabhai <nalin@redhat.com> 20000902-7
- rebuild with proper defines to get support for large lastlog files (#61983)

* Fri Feb 22 2002 Nalin Dahyabhai <nalin@redhat.com> 20000902-6
- rebuild

* Fri Jan 25 2002 Nalin Dahyabhai <nalin@redhat.com> 20000902-5
- fix autoheader breakage and random other things autotools complain about

* Mon Aug 27 2001 Nalin Dahyabhai <nalin@redhat.com> 20000902-4
- use -O0 instead of -O on ia64
- build in source directory
- don't leave lock files on the filesystem when useradd creates a group for
  the user (#50269)
- fix the -o option to check for duplicate UIDs instead of login names (#52187)

* Thu Jul 26 2001 Bill Nottingham <notting@redhat.com> 20000902-3
- build with -O on ia64

* Fri Jun 08 2001 Than Ngo <than@redhat.com> 20000902-2
- fixup broken specfile

* Tue May 22 2001 Bernhard Rosenkraenzer <bero@redhat.com> 20000902-1
- Create an empty mailspool when creating a user so non-setuid/non-setgid
  MDAs (postfix+procmail) can deliver mail (#41811)
- 20000902
- adapt patches

* Fri Mar  9 2001 Nalin Dahyabhai <nalin@redhat.com>
- don't overwrite user dot files in useradd (#19982)
- truncate new files when moving overwriting files with the contents of other
  files while moving directories (keeps files from looking weird later on)
- configure using %%{_prefix} as the prefix

* Fri Feb 23 2001 Trond Eivind Glomsrxd <teg@redhat.com>
- langify

* Wed Aug 30 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix up chage behavior (Bug #15883)

* Wed Aug 30 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 20000826
- Fix up useradd man page (Bug #17036)

* Tue Aug  8 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- check for vipw lock before adding or deleting users (Bug #6489)

* Mon Aug  7 2000 Nalin Dahyabhai <nalin@redhat.com>
- take LOG_CONS out of the openlog() call so that we don't litter the
  screen during text-mode upgrades

* Tue Jul 18 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Remove a fixed-size buffer that caused problems when adding a huge number
  of users to a group (>8192 bytes) (Bugs #3809, #11930)

* Tue Jul 18 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- remove dependency on util-linux because it causes prereq loops

* Tue Jul 18 2000 Nalin Dahyabhai <nalin@redhat.com>
- change symlinked man pages to includers
- require /usr/bin/newgrp (util-linux) so that /usr/bin/sg isn't left dangling

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Matt Wilson <msw@redhat.com>
- use mandir for FHS
- added patches in src/ and po/ to honor DESTDIR
- use make install DESTDIR=$RPM_BUILD_ROOT

* Wed Feb 16 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix up usermod's symlink behavior (Bug #5458)

* Fri Feb 11 2000 Cristian Gafton <gafton@redhat.com>
- get rid of mkpasswd

* Mon Feb  7 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix usermod patch to check for shadow before doing any shadow-specific stuff
  and merge it into the pwlock patch

* Sat Feb  5 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- fix man symlinks

* Wed Feb  2 2000 Nalin Dahyabhai <gafton@redhat.com>
- make -p only change shadow password (bug #8923)

* Mon Jan 31 2000 Cristian Gafton <gafton@redhat.com>
- rebuild to fix dependeencies
- man pages are compressed

* Wed Jan 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix a security bug (adduser could overwrite previously existing
  groups, Bug #8609)

* Sun Jan  9 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- unset LINGUAS before building
- Fix typo in newusers manpage (Bug #8258)
- libtoolize

* Wed Sep 22 1999 Cristian Gafton <gafton@redhat.com>
- fix segfault for userdel when the primary group for the user is not
  defined

* Tue Sep 21 1999 Cristian Gafton <gafton@redhat.com>
- Serial: 1 because now we are using 19990827 (why the heck can't they have
  a normal version just like everybody else?!)
- ported all patches to the new code base

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- SIGHUP nscd from usermod, too

* Fri Apr 09 1999 Michael K. Johnson <johnsonm@redhat.com>
- added usermod password locking from Chris Adams <cadams@ro.com>

* Thu Apr 08 1999 Bill Nottingham <notting@redhat.com>
- have things that modify users/groups SIGHUP nscd on exit

* Wed Mar 31 1999 Michael K. Johnson <johnsonm@redhat.com>
- have userdel remove user private groups when it is safe to do so
- allow -f to force user removal even when user appears busy in utmp

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- edit out unused CHFN fields from login.defs.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 7)

* Wed Jan 13 1999 Bill Nottingham <notting@redhat.com>
- configure fix for arm

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- Note that /usr/sbin/mkpasswd conflicts with /usr/bin/mkpasswd;
  one of these (I think /usr/sbin/mkpasswd but other opinions are valid)
  should probably be renamed.  In any case, mkpasswd.8 from this package
  needs to be installed. (problem #823)

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 980403
- redid the patches

* Tue Dec 30 1997 Cristian Gafton <gafton@redhat.com>
- updated the spec file
- updated the patch so that new accounts created on shadowed system won't
  confuse pam_pwdb anymore ('!!' default password instead on '!')
- fixed a bug that made useradd -G segfault
- the check for the ut_user is now patched into configure

* Thu Nov 13 1997 Erik Troan <ewt@redhat.com>
- added patch for XOPEN oddities in glibc headers
- check for ut_user before checking for ut_name -- this works around some
  confusion on glibc 2.1 due to the utmpx header not defining the ut_name
  compatibility stuff. I used a gross sed hack here because I couldn't make
  automake work properly on the sparc (this could be a glibc 2.0.99 problem
  though). The utuser patch works fine, but I don't apply it.
- sleep after running autoconf

* Thu Nov 06 1997 Cristian Gafton <gafton@redhat.com>
- added forgot lastlog command to the spec file

* Mon Oct 27 1997 Cristian Gafton <gafton@redhat.com>
- obsoletes adduser

* Thu Oct 23 1997 Cristian Gafton <gafton@redhat.com>
- modified groupadd; updated the patch

* Fri Sep 12 1997 Cristian Gafton <gafton@redhat.com>
- updated to 970616
- changed useradd to meet RH specs
- fixed some bugs

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
