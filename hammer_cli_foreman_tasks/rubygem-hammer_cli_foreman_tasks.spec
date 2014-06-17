%global gemname hammer_cli_foreman_tasks

%if 0%{?rhel} < 7
%global gem_dir /usr/lib/ruby/gems/1.8
%endif

%global geminstdir %{gem_dir}/gems/%{gemname}-%{version}

Summary: Contains the code for showing of the tasks (results and progress) in the Hammer CLI
Name: rubygem-%{gemname}
Version: 0.0.3
Release: 2%{?dist}
Group: Development/Languages
License: GPLv3
URL: http://github.com/theforeman/hammer-cli-katello
Source0: %{gemname}-%{version}.gem

%if !( 0%{?rhel} > 6 || 0%{?fedora} > 18 )
Requires: ruby(abi)
%endif
Requires: ruby(rubygems)
Requires: rubygem(hammer_cli_foreman) >= 0.1.1
Requires: rubygem(powerbar)
BuildRequires: ruby(rubygems)
%if 0%{?fedora} || 0%{?rhel} > 6
BuildRequires: rubygems-devel
%endif
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Contains the code for showing of the tasks (results and progress) in the Hammer CLI

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{geminstdir}
%{geminstdir}/lib
%exclude %{gem_dir}/cache/%{gemname}-%{version}.gem
%{gem_dir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.md

%changelog
* Wed May 28 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-2
- update dependencies in rpm spec for 0.1.1 (jmontleo@redhat.com)

* Wed May 28 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-1
- update version to 0.0.3 (jmontleo@redhat.com)
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- bump to version 0.0.3 (komidore64@gmail.com)

* Sat May 17 2014 Jason Montleon <jmontleo@redhat.com> 0.0.2-6
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- async module includable into commands (tstrachota@redhat.com)

* Tue May 06 2014 Jason Montleon <jmontleo@redhat.com> 0.0.2-5
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- ref #4311 - switching all `apipie_options` to `build_options`
  (komidore64@gmail.com)
- ref #4311 - changes to hammer-cli-foreman changed some class names
  (komidore64@gmail.com)

* Mon May 05 2014 Jason Montleon <jmontleo@redhat.com> 0.0.2-4
- remove README (jmontleo@redhat.com)

* Mon May 05 2014 Jason Montleon <jmontleo@redhat.com> 0.0.2-3
- correct macros to work with EL7 (jmontleo@redhat.com)
- Merge remote-tracking branch 'jmontleon/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com> 0.0.2-2
- Merge remote-tracking branch 'upstream/master' (jmontleo@redhat.com)
- fixes #4888 - 1.9 syntax was being used (caught by 1.8 interpreter)
  (komidore64@gmail.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com> 0.0.2-1
- update rpm spec file version to 0.0.2 (jmontleo@redhat.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-1
- update rpm spec file version to 0.0.3 (jmontleo@redhat.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com> 0.0.1-5
- Merge remote-tracking branch 'upstream/master' (jmontleo@redhat.com)
- Bump version (inecas@redhat.com)
- Fixes #4781 - Update to use dynamic bindings (inecas@redhat.com)
- removing specfile in favor of Katello/katello-ballpeen (komidore64@gmail.com)

* Wed Mar 12 2014 Jason Montleon <jmontleo@redhat.com> 0.0.1-4
- new package built with tito

* Thu Feb 27 2014 Jason Montleon <jmontleo@redhat.com> 0.0.1-3
- fix package (jmontleo@redhat.com)

* Thu Feb 27 2014 Jason Montleon <jmontleo@redhat.com> 0.0.1-2
- add unpackaged files to package (jmontleo@redhat.com)
- fix Require for hammer_cli_foreman instead of hammer_cli
  (jmontleo@redhat.com)

* Thu Feb 27 2014 Jason Montleon <jmontleo@redhat.com> 0.0.1-1
- new package built with tito

