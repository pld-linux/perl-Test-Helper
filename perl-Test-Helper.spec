%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Helper
Summary:	Test::Helper perl module
Summary(pl):	Modu� perla Test::Helper
Name:		perl-Test-Helper
Version:	0.002
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Helper perl module - easy creation of test scripts.

%description -l pl
Modu� perla Test::Helper umo�liwia �atwe tworzenie skrypt�w testowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
