%define upstream_name       XML-Entities
%define version 0.0307
%define release %mkrel 1

Name:       perl-%{upstream_name}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Mapping of XML entities to Unicode
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(Fatal)
BuildRequires: perl(File::Basename)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Based upon the HTML::Entities module by Gisle Aas

This module deals with decoding of strings with XML character entities. The
module provides two functions:

* decode( $entity_set, $string, ... )

%prep
%setup -q -n %{upstream_name}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_bindir}/download-entities.pl
%{perl_vendorlib}/XML
%{_mandir}/man1/download-entities.pl.1*
%{_mandir}/man3/*

