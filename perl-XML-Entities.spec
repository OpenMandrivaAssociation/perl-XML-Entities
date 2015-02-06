%define upstream_name    XML-Entities
%define upstream_version 1.0001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Mapping of XML entities to Unicode
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/XML/XML-Entities-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Fatal)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
This module deals with decoding of strings with XML character entities.
Based upon the HTML::Entities module by Gisle Aas

%prep
%setup -q -n %{upstream_name}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes META.yml
%{_bindir}/download-entities.pl
%{perl_vendorlib}/XML
%{_mandir}/man1/download-entities.pl.1*
%{_mandir}/man3/*

%changelog
* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 573808
- update to 1.0000

* Sat Jun 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.0307-1mdv2010.0
+ Revision: 383237
- import perl-XML-Entities


* Fri Jun 05 2009 cpan2dist 0.0307-1mdv
- initial mdv release, generated with cpan2dist


