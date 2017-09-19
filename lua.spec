#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : lua
Version  : 5.3.4
Release  : 39
URL      : http://www.lua.org/ftp/lua-5.3.4.tar.gz
Source0  : http://www.lua.org/ftp/lua-5.3.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: lua-bin
BuildRequires : ncurses-dev
BuildRequires : readline-dev
Patch1: 0001-Build-fixes.patch
Patch2: 0002-Add-lua.pc.patch

%description
This is Lua 5.3.4, released on 12 Jan 2017.
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
Requires: lua-bin
Provides: lua-devel

%description dev
dev components for the lua package.


%prep
%setup -q -n lua-5.3.4
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1504160941
make V=1  %{?_smp_mflags} linux MYCFLAGS="${CFLAGS} -fpic" MYLIBS="-lncurses -lm"

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make test

%install
export SOURCE_DATE_EPOCH=1504160941
rm -rf %{buildroot}
%make_install INSTALL_TOP=%{buildroot}/usr/
## make_install_append content
mkdir -p %{buildroot}/usr/lib64/pkgconfig
cp lua.pc %{buildroot}/usr/lib64/pkgconfig/lua.pc
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/man/man1/lua.1
/usr/man/man1/luac.1

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
