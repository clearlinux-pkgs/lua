#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : lua
Version  : 5.4.4
Release  : 68
URL      : https://www.lua.org/ftp/lua-5.4.4.tar.gz
Source0  : https://www.lua.org/ftp/lua-5.4.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: lua-bin = %{version}-%{release}
Requires: lua-lib = %{version}-%{release}
Requires: lua-man = %{version}-%{release}
BuildRequires : ncurses-dev
BuildRequires : readline-dev
Patch1: 0001-Build-fixes.patch
Patch2: 0002-Add-scimark-as-PGO-profiling-workload.patch
Patch3: 0003-Add-option-for-pgo-profiling-test-with-scimark.patch

%description
This is Lua 5.4.4, released on 13 Jan 2022.
For installation instructions, license details, and
further information about Lua, see doc/readme.html.

%package bin
Summary: bin components for the lua package.
Group: Binaries

%description bin
bin components for the lua package.


%package dev
Summary: dev components for the lua package.
Group: Development
Requires: lua-lib = %{version}-%{release}
Requires: lua-bin = %{version}-%{release}
Provides: lua-devel = %{version}-%{release}
Requires: lua = %{version}-%{release}

%description dev
dev components for the lua package.


%package lib
Summary: lib components for the lua package.
Group: Libraries

%description lib
lib components for the lua package.


%package man
Summary: man components for the lua package.
Group: Default

%description man
man components for the lua package.


%package staticdev
Summary: staticdev components for the lua package.
Group: Default
Requires: lua-dev = %{version}-%{release}

%description staticdev
staticdev components for the lua package.


%prep
%setup -q -n lua-5.4.4
cd %{_builddir}/lua-5.4.4
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667413574
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" LDFLAGS="${LDFLAGS_GENERATE}"
make  %{?_smp_mflags}  linux-readline MYCFLAGS="${CFLAGS} -fpic -DLUA_COMPAT_5_2 -DLUA_COMPAT_5_1" MYLDFLAGS="${CFLAGS}" MYLIBS="-lncurses -lm"

make test_pgo
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" LDFLAGS="${LDFLAGS_USE}"
make  %{?_smp_mflags}  linux-readline MYCFLAGS="${CFLAGS} -fpic -DLUA_COMPAT_5_2 -DLUA_COMPAT_5_1" MYLDFLAGS="${CFLAGS}" MYLIBS="-lncurses -lm"


%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make test

%install
export SOURCE_DATE_EPOCH=1667413574
rm -rf %{buildroot}
%make_install INSTALL_TOP=%{buildroot}/usr/

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lua
/usr/bin/luac

%files dev
%defattr(-,root,root,-)
/usr/include/lauxlib.h
/usr/include/lua.h
/usr/include/lua.hpp
/usr/include/luaconf.h
/usr/include/lualib.h
/usr/lib64/liblua.so
/usr/lib64/pkgconfig/lua.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblua.so.5.4
/usr/lib64/liblua.so.5.4.4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lua.1
/usr/share/man/man1/luac.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/liblua.a
