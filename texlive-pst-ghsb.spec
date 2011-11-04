# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-pst-ghsb
Version:	20111104
Release:	1
Summary:	TeXLive pst-ghsb package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ghsb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ghsb.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive pst-ghsb package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-ghsb/pst-ghsb.pro
%{_texmfdistdir}/tex/generic/pst-ghsb/pst-ghsb.tex
%{_texmfdistdir}/tex/latex/pst-ghsb/pst-ghsb.sty
%doc %{_texmfdistdir}/doc/generic/pst-ghsb/README
%doc %{_texmfdistdir}/doc/generic/pst-ghsb/t-ghsb.pdf
%doc %{_texmfdistdir}/doc/generic/pst-ghsb/t-ghsb.tex
%doc %{_texmfdistdir}/doc/generic/pst-ghsb/t2-ghsb.pdf
%doc %{_texmfdistdir}/doc/generic/pst-ghsb/t2-ghsb.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
