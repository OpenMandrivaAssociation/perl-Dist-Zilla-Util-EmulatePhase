%define upstream_name    Dist-Zilla-Util-EmulatePhase
%define upstream_version 0.01003312

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A dummy Dist::Zilla to fake a 'prereq' object on
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Dist::Zilla::Prereqs)
BuildRequires: perl(Dist::Zilla::Util::Test::KENTNL) >= 0.10.5.100
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Hash::Merge::Simple)
BuildRequires: perl(Module::Build) >= 0.360.100
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Autobox)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::Fatal) >= 0.3.0
BuildRequires: perl(Test::More) >= 0.96
BuildRequires: perl(Try::Tiny)
BuildRequires: perl(namespace::autoclean)
BuildArch:  noarch

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

#%check
#./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.json META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*

