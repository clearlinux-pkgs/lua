#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : lua
Version  : 5.3.5
Release  : 49
URL      : http://www.lua.org/ftp/lua-5.3.5.tar.gz
Source0  : http://www.lua.org/ftp/lua-5.3.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: lua-bin = %{version}-%{release}
Requires: lua-man = %{version}-%{release}
BuildRequires : ncurses-dev
BuildRequires : readline-dev
Patch1: 0001-Build-fixes.patch
Patch2: 0002-Add-lua.pc.patch
Patch3: CVE-2019-6706.patch

%description
This is Lua 5.3.5, released on 26 Jun 2018.
For installation instructions, license details, and
further information about Lua, see doc/readme.html.

%package bin
Summary: bin components for the lua package.
Group: Binaries
Requires: lua-man = %{version}-%{release}

%description bin
bin components for the lua package.


%package dev
Summary: dev components for the lua package.
Group: Development
Requires: lua-bin = %{version}-%{release}
Provides: lua-devel = %{version}-%{release}

%description dev
dev components for the lua package.


%package man
Summary: man components for the lua package.
Group: Default

%description man
man components for the lua package.


%prep
%setup -q -n lua-5.3.5
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548286912
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
make  %{?_smp_mflags} linux MYCFLAGS="${CFLAGS} -fpic" MYLIBS="-lncurses -lm"


%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make test

%install
export SOURCE_DATE_EPOCH=1548286912
rm -rf %{buildroot}
%make_install INSTALL_TOP=%{buildroot}/usr/
## install_append content
mkdir -p %{buildroot}/usr/lib64/pkgconfig
cp lua.pc %{buildroot}/usr/lib64/pkgconfig/lua.pc
mkdir -p %{buildroot}/usr/share
mv %{buildroot}/usr/man %{buildroot}/usr/share/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lua
/usr/bin/luac

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/*.hpp
/usr/lib64/*.a
/usr/lib64/pkgconfig/lua.pc

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lua.1
/usr/share/man/man1/luac.1
