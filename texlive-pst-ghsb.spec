# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-pst-ghsb
Version:	20180303
Release:	2
Summary:	TeXLive pst-ghsb package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ghsb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ghsb.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive pst-ghsb package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 755311
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719356
- texlive-pst-ghsb
- texlive-pst-ghsb
- texlive-pst-ghsb
- texlive-pst-ghsb

