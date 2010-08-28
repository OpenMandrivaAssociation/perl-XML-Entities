%define upstream_name    XML-Entities
%define upstream_version 1.0000

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Mapping of XML entities to Unicode
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Fatal)
BuildRequires: perl(File::Basename)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This module deals with decoding of strings with XML character entities.
Based upon the HTML::Entities module by Gisle Aas

%prep
%setup -q -n %{upstream_name}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes META.yml
%{_bindir}/download-entities.pl
%{perl_vendorlib}/XML
%{_mandir}/man1/download-entities.pl.1*
%{_mandir}/man3/*
