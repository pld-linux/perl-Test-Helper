%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Helper
Summary:	Test::Helper - easy creation of test scripts
Summary(pl.UTF-8):   Test::Helper - łatwe tworzenie skryptów testowych
Name:		perl-Test-Helper
Version:	0.002
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5a08c6c7e790b72f6635e8db4c43c7b7
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Helper Perl module is for easy creation of test scripts.

%description -l pl.UTF-8
Moduł Perla Test::Helper umożliwia łatwe tworzenie skryptów testowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Test/Helper.pm
%{_mandir}/man3/*
