%include	/usr/lib/rpm/macros.perl
Summary:	Test-Helper perl module
Summary(pl):	Modu³ perla Test-Helper
Name:		perl-Test-Helper
Version:	0.002
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/Test-Helper-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test-Helper perl module - easy creation of test scripts.

%description -l pl
Modu³ perla Test-Helper umo¿liwia ³atwe tworzenie skryptów testowych.

%prep
%setup -q -n Test-Helper-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Test/Helper.pm
%{_mandir}/man3/*
