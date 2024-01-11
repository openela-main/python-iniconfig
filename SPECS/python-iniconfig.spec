Name:               python-iniconfig
Version:            1.1.1
Release:            2%{?dist}
Summary:            Brain-dead simple parsing of ini files
License:            MIT
URL:                http://github.com/RonnyPfannschmidt/iniconfig

BuildArch:          noarch
# Exclude i686 arch. Due to a modularity issue it's being added to the
# x86_64 compose of CRB, but we don't want to ship it at all.
# See: https://projects.engineering.redhat.com/browse/RCM-72605
ExcludeArch:        i686

BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-rpm-macros
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python%{python3_pkgversion}-wheel

Source0:            %{pypi_source iniconfig}

# pytest 6+ needs this and this uses pytest for tests
%bcond_without tests

%if %{with tests}
BuildRequires:      python%{python3_pkgversion}-pytest
%endif

%global _description %{expand:
iniconfig is a small and simple INI-file parser module
having a unique set of features:

* tested against Python2.4 across to Python3.2, Jython, PyPy
* maintains order of sections and entries
* supports multi-line values with or without line-continuations
* supports "#" comments everywhere
* raises errors with proper line-numbers
* no bells and whistles like automatic substitutions
* iniconfig raises an Error if two sections have the same name.}
%description %_description


%package -n python%{python3_pkgversion}-iniconfig
Summary:            %{summary}
%description -n python%{python3_pkgversion}-iniconfig %_description


%prep
%autosetup -n iniconfig-%{version}

# Remove dependency of setuptools-scm
sed -i "s/ *use_scm_version=.*,/version='%{version}',/" setup.py


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
%pytest
%endif


%files -n python%{python3_pkgversion}-iniconfig
%doc README.txt
%license LICENSE
%{python3_sitelib}/iniconfig-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/iniconfig/


%changelog
* Wed Jan 13 2021 Tomas Orsava <torsava@redhat.com> - 1.1.1-2
- Convert from Fedora to the python39 module in RHEL8
- Revert usage of pyproject-rpm-macros
- Remove dependency on setuptools_scm
- Resolves: rhbz#1877430

* Thu Oct 15 2020 Tomas Hrnciar <thrnciar@redhat.com> - 1.1.1-1
- Update to 1.1.1 (#1888157)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-1
- Initial package (#1856421)
