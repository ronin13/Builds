%define _default_patch_fuzz 2
Summary: A text mode mail and news user agent
Name: mutt
Version: 1.5.21
Release: 1.nntp
Epoch: 5
License: GPLv2+ and Public Domain
Group: Applications/Internet
Source: ftp://ftp.mutt.org/mutt/%{name}-%{version}.tar.gz
Patch0: %{name}-%{version}.rr.compressed
Patch1: %{name}-%{version}.vvv.nntp
Patch2: %{name}-%{version}.vvv.initials
Patch3: %{name}-%{version}.vvv.quote
Patch4: %{name}-%{version}.vvv.ru
Url: http://www.mutt.org/
BuildPrereq: slang-devel >= 0.99.38, gettext, openssl-devel, automake
BuildPrereq: docbook-style-xsl, libxslt, gdbm-devel
Requires: slang >= 0.99.38, smtpdaemon, openssl, gdbm
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Mutt is a text mode mail and news user agent. Mutt supports color,
threading, arbitrary key remapping, and a lot of customization.

You should install mutt if you've used mutt in the past and you prefer
it, or if you're new to mail programs and you haven't decided which
one you're going to use.

%prep
%setup -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
aclocal -I m4
autoheader
automake --foreign
autoconf
export -n LINGUAS
CFLAGS="$RPM_OPT_FLAGS -O0" LDFLAGS=-s ./configure \
	--prefix=/usr --mandir=/usr/share/man \
	--with-sharedir=/etc --sysconfdir=/etc \
	--with-docdir=/usr/share/doc/%{name}-%{version} \
	--enable-pop --enable-imap --enable-smtp --enable-nntp \
	--enable-hcache --enable-debug \
	--with-ssl --enable-compressed --with-slang --without-wc-funcs
make
cd doc
make Muttrc

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
install -m 644 ABOUT-NLS BEWARE *.nntp contrib/language* $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
mv $RPM_BUILD_ROOT/etc/mime.types $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/samples/sample.mime.types
rm -f $RPM_BUILD_ROOT/etc/*.dist

%find_lang %{name}

%files -f %{name}.lang
%config /etc/Muttrc
%doc /usr/share/doc
%attr(-,-,mail) %{_bindir}/mutt_dotlock
%{_bindir}/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%changelog
* Wed Sep 16 2010 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.21

* Thu Aug 13 2009 Vsevolod Volkov <vvv@mutt.org.ua>
- nntp patch: fixed writting references in nntp_save_cache_group()
- quote patch: code moved to text_plain_handler()

* Tue Jun 15 2009 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.20
- nntp patch: save Date: header of recorded outgoing articles

* Tue Jan  6 2009 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.19

* Mon May 19 2008 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.18
- urlview removed
- nntp patch: fixed SIGSEGV when followup or forward to newsgroup

* Sun Nov  4 2007 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.17

* Tue Jul  3 2007 Vsevolod Volkov <vvv@mutt.org.ua>
- nntp patch: fixed arguments of nntp_format_str()

* Fri Jun 15 2007 Vsevolod Volkov <vvv@mutt.org.ua>
- nntp patch: fixed error selecting news group

* Tue Jun 12 2007 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.16

* Wed Apr 11 2007 Vsevolod Volkov <vvv@mutt.org.ua>
- smtp support enabled
- nntp patch: fixed posting error if $smtp_url is set
- nntp patch: added support of print-style sequence %R (x-comment-to)

* Sun Apr  8 2007 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.15
- header cache support enabled
- nntp patch: nntp://... url changed to news://...
- nntp patch: added indicator of fetching descriptions progress

* Tue Feb 28 2007 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.14

* Tue Aug 15 2006 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.13

* Mon Jul 17 2006 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.12
- nntp patch: fixed reading empty .newsrc

* Sat Sep 17 2005 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.11

* Sun Aug 28 2005 Vsevolod Volkov <vvv@mutt.org.ua>
- remove wmconfig support
- fixed group of mutt_dotlock

* Sat Aug 13 2005 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.10

* Tue Jun 28 2005 Vsevolod Volkov <vvv@mutt.org.ua>
- rebuild for Fedora Core 4

* Sun Mar 13 2005 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.9

* Sun Feb 13 2005 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.8

* Sat Feb  5 2005 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.7
- nntp patch: function mutt_update_list_file() moved to newsrc.c and changed algorithm
- nntp patch: fixed error in nntp_logout_all()
- nntp patch: fixed debug output in mutt_newsrc_update()
- nntp patch: added optional support of LISTGROUP command
- nntp patch: fixed typo in nntp_parse_xref()

* Sun Aug 15 2004 Vsevolod Volkov <vvv@mutt.org.ua>
- urlview added

* Tue Feb  3 2004 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.6

* Thu Dec 18 2003 Vsevolod Volkov <vvv@mutt.org.ua>
- compose patch: fixed compose menu in nntp patch

* Thu Nov  6 2003 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.5.1

* Wed Nov  5 2003 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.5
- nntp patch: added space after newsgroup name in .newsrc file

* Sun May 18 2003 Vsevolod Volkov <vvv@mutt.org.ua>
- nntp patch: fixed SIGSEGV when posting article

* Sat Mar 22 2003 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.4

* Sat Dec 21 2002 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.3
- nntp patch: replace safe_free calls by the FREE macro

* Fri Dec  6 2002 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.2
- nntp patch: nntp authentication can be passed after any command

* Sat May  4 2002 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.5.1

* Thu May  2 2002 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.99

* Wed Mar 13 2002 Vsevolod Volkov <vvv@mutt.org.ua>
- nntp patch: update to 1.3.28
- nntp patch: fixed SIGSEGV in <get-message>, <get-parent>, <get-children>,
  <reconstruct-thread> functions
- nntp patch: fixed message about nntp reconnect
- nntp patch: fixed <attach-news-message> function using browser
- nntp patch: added support of Followup-To: poster
- nntp patch: added %n (new articles) in group_index_format
- nntp patch: posting articles without inews by default
- removed ru patch

* Wed Jan 23 2002 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.27

* Fri Jan 18 2002 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.26

* Thu Jan  3 2002 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.25
- nntp patch: accelerated speed of access to news->newsgroups hash
- nntp patch: added default content disposition

* Mon Dec  3 2001 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.24

* Fri Nov  9 2001 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.23.2
- nntp patch: fixed segfault if mutt_conn_find() returns null

* Wed Oct 31 2001 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.23.1
- nntp patch: added support of LISTGROUP command
- nntp patch: added support for servers with broken overview
- nntp patch: disabled <flag-message> function on news server
- nntp patch: fixed error storing bad authentication information

* Wed Oct 10 2001 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.23
- nntp patch: fixed typo in buffy.c
- nntp patch: added substitution of %s parameter in $inews variable

* Fri Aug 31 2001 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.22.1
- update to 1.3.22

* Thu Aug 23 2001 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.21

* Wed Jul 25 2001 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.20
- nntp patch: removed 'server-hook', use 'account-hook' instead
- nntp patch: fixed error opening NNTP server without newsgroup using -f option

* Fri Jun  8 2001 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.19

* Sun May  6 2001 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.18
- nntp patch: fixed typo in nntp_attempt_features()
- nntp patch: changed algorithm of XGTITLE command testing
- nntp patch: disabled writing of NNTP password in debug file
- nntp patch: fixed reading and writing of long newsrc lines
- nntp patch: changed checking of last line while reading lines from server
- nntp patch: fixed possible buffer overrun in nntp_parse_newsrc_line()
- nntp patch: removed checking of XHDR command
- nntp patch: compare NNTP return codes without trailing space

* Thu Mar 29 2001 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.17
- nntp patch: support for 'LIST NEWSGROUPS' command to read descriptions
- removed patch instdoc
- removed patch sslretry

* Sat Mar  3 2001 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.16
- added patch: instdoc - missing instdoc.sh.in
- added patch: sslretry - fixes compilation error with openssl < 0.9.6

* Wed Feb 14 2001 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.15

* Sun Jan 28 2001 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.14
- nntp patch: show number of tagged messages patch from
  Felix von Leitner <leitner@fefe.de>

* Sun Dec 31 2000 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.13
- nntp patch: fixed problem if last article in group is deleted
- nntp patch: fixed checking of XGTITLE command on some servers
- nntp patch: added \r in AUTHINFO commands

* Mon Nov 27 2000 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.12

* Wed Nov  1 2000 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.11
- nntp patch: fixed error opening newsgroup from mutt started with -g or -G

* Thu Oct 12 2000 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.10
- nntp patch: hotkey 'G' (get-message) replaced with '^G'

* Thu Sep 21 2000 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.9
- nntp patch: changed delay displaying error messages from 1 to 2 seconds
- nntp patch: fixed error compiling with nntp and without imap
- removed mutt-1.3.8.default_charset patch

* Wed Sep  6 2000 Vsevolod Volkov <vvv@mutt.org.ua>
- nntp patch: fixed catchup in index
- nntp patch: fixed nntp_open_mailbox()

* Sat Sep  2 2000 Vsevolod Volkov <vvv@mutt.org.ua>
- nntp patch: functions <edit> and <delete-entry> disabled
- nntp patch: format of news mailbox names changed to url form
- nntp patch: option nntp_attempts removed
- nntp patch: option reconnect_news renamed to nntp_reconnect
- nntp patch: default value of nntp_poll changed from 30 to 60
- nntp patch: error handling improved

* Wed Aug 30 2000 Vsevolod Volkov <vvv@mutt.org.ua>
- update to 1.3.8
- nntp patch: new option show_only_unread
- nntp patch: add newsgroup completion

* Fri Aug  4 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.3.7

* Mon Jul 31 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.3.6

* Sun Jul  9 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.3.5
- nntp patch: authentication code update
- nntp patch: fix for changing to newsgroup from mailbox with read messages
- nntp patch: socket code optimization
- removed mutt-1.3.4.tlr.curslib_m4 patch

* Wed Jun 21 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.3.4
- added mutt-1.3.4.tlr.curslib_m4 patch
- removed mutt-1.3.3.ege.send_charsets patch

* Thu Jun 15 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- removed mutt-1.3.3.vvv.change_charset patch
- updated mutt-1.3.3.vvv.ru patch

* Wed Jun 14 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- updated mutt-1.3.3.vvv.initials patch
- updated mutt-1.3.3.vvv.quote patch
- updated mutt-1.3.3.vvv.ru patch
- added mutt-1.3.3.ege.send_charsets patch
- update to 1.3.3
- nntp patch: substitution of newsgroup after reconnection
- nntp patch: loading newsgroups with very long names
- nntp patch: loading more than 32768 newsgroups
- nntp patch: don't substitute current newsgroup with deleted
  new messages

* Tue May 30 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- updated mutt-1.3.2.change_charset patch

* Wed May 24 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- added mutt-1.3.2.vvv.charset_hook patch
- update to 1.3.2
- added mutt-1.3.1.vvv.parse_overflow patch

* Sat May 20 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.3.1

* Thu May 18 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- updated mutt-1.3.vvv.ru patch

* Fri May 12 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.3

* Thu May 11 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.2

* Thu May  4 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.1.14
- removed gpg-2comp

* Sun Apr 23 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.1.12

* Wed Apr 12 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- replaced patch mutt-1.1.11.browser with mutt-1.1.11.vvv.browser
- added mutt-1.1.11.vvv.yes_no patch
- nntp patch: add substitution of newsgroup with new messages

* Wed Apr  5 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- nntp patch: add attach message from newsgroup
- nntp patch: add one-line help in newsreader mode
- nntp patch: disable 'change-dir' command in newsgroups browser
- nntp patch: add options -g and -G
- nntp patch: get default newsserver from file /etc/nntpserver
- nntp patch: add print-style sequence %s to $newsrc

* Thu Mar 30 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.1.11
- update to 1.1.10

* Thu Mar 23 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- nntp patch: remove 'toggle-mode' function
- nntp patch: add 'change-newsgroup' function
- nntp patch: fix server-hook
- nntp patch: fix error 'bounce' function after 'post'
- nntp patch: add 'forward to newsgroup' function
- nntp patch: 'forward' function works in newsreader mode
- nntp patch: add 'post' and 'followup' functions to pager
  and attachment menu
- nntp patch: fix active descriptions and allowed flag reload

* Fri Mar 17 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- initials patch: fix segfault replying to attached message

* Tue Mar 14 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.1.9
- nntp patch: remove deleted newsgroups from list
- nntp patch: update .newsrc in browser
- nntp patch: reload .newsrc if externally modified
- nntp patch: fix active cache update

* Sun Mar  5 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.1.8

* Sat Mar  4 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- removed *.ag.addrbook-comment and *.update_list_file patches
- nntp patch: count lines when loading descriptions
- nntp patch: remove cache of unsubscribed newsgroups
- nntp patch: load list of newsgroups from cache faster

* Thu Mar  2 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.1.7

* Tue Feb 29 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- nntp patch: fix unread messages in browser
- nntp patch: fix message status
- nntp patch: fix updating new messages in cache

* Fri Feb 25 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.1.5
- nntp patch: fix updating new messages in cache

* Mon Feb 21 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- nntp patch: change default cache filenames
- nntp patch: fix updating new messages in cache
- quote patch: fix segmentation fault if quote long lines
- added mutt-1.1.4.change.rcvd.charset patch

* Fri Feb 18 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- nntp patch: fix segmentation fault in news groups browser

* Tue Feb 15 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.1.4

* Tue Feb 15 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- updated locking in mutt-1.1.3.rr.compressed patch

* Sun Feb 13 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- added mutt-1.1.3.rr.compressed patch

* Thu Feb 10 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.1.3

* Mon Jan 31 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- recompiled with gnupg support
- added mutt-1.1.2.empty-myhdr patch

* Sun Jan 30 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- nntp patch: X-Comment-To editing

* Fri Jan 28 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.1.2

* Thu Jan 20 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- added mutt-1.1.1.initials and mutt-1.1.1.quote patches

* Mon Jan  3 2000 Vsevolod Volkov <vvv@mutt.kiev.ua>
- added mutt-1.1.1.y2k patch

* Wed Dec 22 1999 Vsevolod Volkov <vvv@mutt.kiev.ua>
- added mutt-0.9* and mutt-1.1.1.news-subject patches

* Tue Dec 21 1999 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.1.1 with news patch

* Sat Nov 27 1999 Vsevolod Volkov <vvv@mutt.kiev.ua>
- update to 1.1 with news patch

* Fri Sep 25 1999 Bill Nottingham <notting@redhat.com>
- add a buffer overflow patch

* Tue Aug 31 1999 Bill Nottingham <notting@redhat.com>
- update to 1.0pre2

* Tue Aug 17 1999 Bill Nottingham <notting@redhat.com>
- update to 0.95.7
- require urlview since the default muttrc uses it

* Mon Jun 21 1999 Bill Nottingham <notting@redhat.com>
- get correct manual path the Right Way(tm)
- make it so it uses default colors even if COLORFGBG isn't set

* Mon Jun 14 1999 Bill Nottingham <notting@redhat.com>
- update to 0.95.6

* Mon Apr 26 1999 Bill Nottingham <notting@redhat.com>
- try and make sure $RPM_OPT_FLAGS gets passed through

* Fri Apr 23 1999 Bill Nottingham <notting@redhat.com>
- update to 0.95.5

* Mon Mar 29 1999 Bill Nottingham <notting@redhat.com>
- sed correct doc path into /etc/Muttrc for viewing manual

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Mar 18 1999 Bill Nottingham <notting@redhat.com>
- strip binary

* Mon Mar  8 1999 Bill Nottingham <notting@redhat.com>
- update to 0.95.4 - fixes a /tmp race

* Wed Feb 24 1999 Bill Nottingham <notting@redhat.com>
- the RETURN OF WMCONFIG! Aiyeee!

* Fri Feb 12 1999 Bill Nottingham <notting@redhat.com>
- 0.95.3 - fixes mailcap handling

* Mon Jan  4 1999 Bill Nottingham <notting@redhat.com>
- 0.95.1

* Sat Dec 12 1998 Bill Nottingham <notting@redhat.com>
- 0.95

* Fri Jul 31 1998 Bill Nottingham <notting@redhat.com>
- backport some 0.94.2 security fixes
- fix un-setgid
- update to 0.93.2

* Tue Jul 28 1998 Jeff Johnson <jbj@redhat.com>
- security fix
- update to 0.93.1.
- turn off setgid mail.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.91.1

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to mutt-0.89.1

* Thu Oct 16 1997 Otto Hammersmith <otto@redhat.com>
- Updated to mutt 0.85.
- added wmconfig entries.
- removed mime.types

* Mon Sep 1 1997 Donnie Barnes <djb@redhat.com>
- Rebuilt to insure all sources were fresh and patches were clean.

* Wed Aug 6 1997 Manoj Kasichainula <manojk@io.com>
- Initial version for 0.81(e)
