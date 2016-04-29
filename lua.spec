#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lua
Version  : 5.3.2
Release  : 18
URL      : http://www.lua.org/ftp/lua-5.3.2.tar.gz
Source0  : http://www.lua.org/ftp/lua-5.3.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: lua-bin
BuildRequires : ncurses-dev
BuildRequires : readline-dev
Patch1: build.patch

%description
This is Lua 5.3.2, released on 25 Nov 2015.
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
%setup -q -n lua-5.3.2
%patch1 -p1

%build
make V=1  %{?_smp_mflags} linux

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make test

%install
rm -rf %{buildroot}
%make_install INSTALL_TOP=%{buildroot}/usr/
## make_install_append content
mkdir -p %{_buildroot}/usr/lib64/pkgconfig
make pc INSTALL_TOP=/usr > %{_buildroot}/usr/lib64/pkgconfig/lua.pc
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
