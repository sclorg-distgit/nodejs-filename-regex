%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name filename-regex

Summary:       Regular expression for matching file names
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       2.0.0
Release:       2%{?dist}
License:       MIT
URL:           https://github.com/regexps/filename-regex
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs010-runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Regular expression for matching file names, with or without extension.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%{nodejs_sitelib}/%{npm_name}

%changelog
* Mon Jan 11 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-2
- Enable scl macros

* Tue Dec 15 2015 Troy Dawson <tdawson@redhat.com> - 2.0.0-1
- Initial package