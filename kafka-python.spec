Name:           python-kafka
Version:        %{major_version}
Release:        %{minor_version}%{?dist}
Url:            http://github.com/mumrah/kafka-python
Summary:        Python 2 client for Apache Kafka
License:        ASL 2.0
Source0:        rpmpkg-src.tar.gz
Requires:       python-six, python-snappy
BuildArch:      noarch

%description
This module provides low-level protocol support for Apache Kafka as well as
high-level consumer and producer classes.  Request batching is supported by
the protocol as well as broker-aware request routing.  Gzip and Snappy
compression is also supported for message sets.

%if %{?python3_sitelib:1}0
%package -n     python3-kafka
Summary:        Python 3 client for Apache Kafka
Requires:       python3-six, python3-snappy
Obsoletes:      kafka-python
Provides:       kafka-python
BuildArch:      noarch

%description -n python3-kafka
This module provides low-level protocol support for Apache Kafka as well as
high-level consumer and producer classes.  Request batching is supported by
the protocol as well as broker-aware request routing.  Gzip and Snappy
compression is also supported for message sets.
%endif


%prep
%setup -q -n kafka-python


%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%if %{?python3_sitelib:1}0
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%endif


%files
%defattr(-,root,root,-)
%doc AUTHORS.md CHANGES.md LICENSE README.rst
%{python_sitelib}/*

%if %{?python3_sitelib:1}0
%files -n python3-kafka
%defattr(-,root,root,-)
%doc AUTHORS.md CHANGES.md LICENSE README.rst
%{python3_sitelib}/*
%endif


%changelog
* Thu Sep 24 2015 Oskari Saarenmaa <os@ohmu.fi> - 0.9.5-0
- Initial
