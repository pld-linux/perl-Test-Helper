%include	/usr/lib/rpm/macros.perl
Summary:	Test-Helper perl module
Summary(pl):	Modu³ perla Test-Helper
Name:		perl-Test-Helper
Version:	0.002
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/Test-Helper-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Test-Helper perl module - easy creation of test scripts.

%description -l pl
Modu³ perla Test-Helper umo¿liwia ³atwe tworzenie skryptów testowych.

%prep
%setup -q -n Test-Helper-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Test/Helper
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* 
        

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%{perl_sitelib}/Test/Helper.pm
%{perl_sitearch}/auto/Test/Helper

%{_mandir}/man3/*
