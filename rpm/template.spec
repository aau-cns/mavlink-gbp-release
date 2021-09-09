%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-mavlink
Version:        2021.9.9
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mavlink package

License:        LGPLv3
URL:            https://mavlink.io/en/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-catkin
BuildRequires:  cmake
BuildRequires:  python3-devel
BuildRequires:  python3-future
BuildRequires:  python3-lxml
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
MAVLink message marshaling library. This package provides C-headers and C++11
library for both 1.0 and 2.0 versions of protocol. For pymavlink use separate
install via rosdep (python-pymavlink).

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/noetic

%changelog
* Thu Sep 09 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.9.9-1
- Autogenerated by Bloom

* Sun Aug 08 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.8.8-1
- Autogenerated by Bloom

* Wed Jul 07 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.7.7-1
- Autogenerated by Bloom

* Sun Jun 06 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.6.6-1
- Autogenerated by Bloom

* Wed May 05 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.5.5-1
- Autogenerated by Bloom

* Mon Apr 05 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.4.5-1
- Autogenerated by Bloom

* Wed Mar 03 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.3.3-1
- Autogenerated by Bloom

* Mon Feb 15 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.2.15-1
- Autogenerated by Bloom

* Tue Feb 02 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.2.2-1
- Autogenerated by Bloom

* Mon Jan 04 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.1.4-1
- Autogenerated by Bloom

* Sat Dec 12 2020 Vladimir Ermakov <vooon341@gmail.com> - 2020.12.12-1
- Autogenerated by Bloom

* Wed Nov 11 2020 Vladimir Ermakov <vooon341@gmail.com> - 2020.11.11-1
- Autogenerated by Bloom

* Sun Oct 11 2020 Vladimir Ermakov <vooon341@gmail.com> - 2020.10.11-2
- Autogenerated by Bloom

* Sun Oct 11 2020 Vladimir Ermakov <vooon341@gmail.com> - 2020.10.11-1
- Autogenerated by Bloom

* Thu Sep 10 2020 Vladimir Ermakov <vooon341@gmail.com> - 2020.9.10-1
- Autogenerated by Bloom

* Sat Aug 08 2020 Vladimir Ermakov <vooon341@gmail.com> - 2020.8.8-1
- Autogenerated by Bloom

* Tue Jul 07 2020 Vladimir Ermakov <vooon341@gmail.com> - 2020.7.7-1
- Autogenerated by Bloom

* Sat Jun 06 2020 Vladimir Ermakov <vooon341@gmail.com> - 2020.6.6-1
- Autogenerated by Bloom

* Thu May 21 2020 Vladimir Ermakov <vooon341@gmail.com> - 2020.5.21-1
- Autogenerated by Bloom

* Tue May 05 2020 Vladimir Ermakov <vooon341@gmail.com> - 2020.5.5-1
- Autogenerated by Bloom

