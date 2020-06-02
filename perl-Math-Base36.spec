#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Math-Base36
Version  : 0.14
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/B/BR/BRICAS/Math-Base36-0.14.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BR/BRICAS/Math-Base36-0.14.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmath-base36-perl/libmath-base36-perl_0.14-1.debian.tar.xz
Summary  : 'Encoding and decoding of base36 strings'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Math-Base36-license = %{version}-%{release}
Requires: perl-Math-Base36-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Install)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)

%description
NAME
Math::Base36 - Encoding and decoding of base36 strings
SYNOPSIS
use Math::Base36 ':all';

%package dev
Summary: dev components for the perl-Math-Base36 package.
Group: Development
Provides: perl-Math-Base36-devel = %{version}-%{release}
Requires: perl-Math-Base36 = %{version}-%{release}

%description dev
dev components for the perl-Math-Base36 package.


%package license
Summary: license components for the perl-Math-Base36 package.
Group: Default

%description license
license components for the perl-Math-Base36 package.


%package perl
Summary: perl components for the perl-Math-Base36 package.
Group: Default
Requires: perl-Math-Base36 = %{version}-%{release}

%description perl
perl components for the perl-Math-Base36 package.


%prep
%setup -q -n Math-Base36-0.14
cd %{_builddir}
tar xf %{_sourcedir}/libmath-base36-perl_0.14-1.debian.tar.xz
cd %{_builddir}/Math-Base36-0.14
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Math-Base36-0.14/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Math-Base36
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Math-Base36/24b216d481caa6823ffb92f9e93701b0c9a4651a
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Math::Base36.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Math-Base36/24b216d481caa6823ffb92f9e93701b0c9a4651a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Math/Base36.pm
