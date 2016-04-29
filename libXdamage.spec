#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libXdamage
Version  : 1.1.4
Release  : 5
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXdamage-1.1.4.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXdamage-1.1.4.tar.bz2
Summary  : X Damage  Library
Group    : Development/Tools
License  : MIT
Requires: libXdamage-lib
BuildRequires : pkgconfig(damageproto)
BuildRequires : pkgconfig(fixesproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xorg-macros)

%description
Damage
X Damage Extension
Version 1.1
2007-01-04
This package contains the library for the X Damage extension.

%package dev
Summary: dev components for the libXdamage package.
Group: Development
Requires: libXdamage-lib

%description dev
dev components for the libXdamage package.


%package lib
Summary: lib components for the libXdamage package.
Group: Libraries

%description lib
lib components for the libXdamage package.


%prep
%setup -q -n libXdamage-1.1.4

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/Xdamage.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
