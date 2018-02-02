#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libXdamage
Version  : 1.1.4
Release  : 11
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXdamage-1.1.4.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXdamage-1.1.4.tar.bz2
Summary  : X Damage  Library
Group    : Development/Tools
License  : HPND
Requires: libXdamage-lib
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32damageproto)
BuildRequires : pkgconfig(32fixesproto)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xextproto)
BuildRequires : pkgconfig(32xfixes)
BuildRequires : pkgconfig(32xorg-macros)
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
Provides: libXdamage-devel

%description dev
dev components for the libXdamage package.


%package dev32
Summary: dev32 components for the libXdamage package.
Group: Default
Requires: libXdamage-lib32
Requires: libXdamage-dev

%description dev32
dev32 components for the libXdamage package.


%package lib
Summary: lib components for the libXdamage package.
Group: Libraries

%description lib
lib components for the libXdamage package.


%package lib32
Summary: lib32 components for the libXdamage package.
Group: Default

%description lib32
lib32 components for the libXdamage package.


%prep
%setup -q -n libXdamage-1.1.4
pushd ..
cp -a libXdamage-1.1.4 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491879573
export CFLAGS="$CFLAGS -Os -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1491879573
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/Xdamage.h
/usr/lib64/libXdamage.so
/usr/lib64/pkgconfig/xdamage.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXdamage.so
/usr/lib32/pkgconfig/32xdamage.pc
/usr/lib32/pkgconfig/xdamage.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXdamage.so.1
/usr/lib64/libXdamage.so.1.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXdamage.so.1
/usr/lib32/libXdamage.so.1.1.0
