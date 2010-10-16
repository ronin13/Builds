
This is mutt build with :

Patches used:
compressed
sidebar
initials
quote
nntp


nntp and sidebar patches for 1.5.21 were conflicting. Fixed them.


Features:
    -ssl
    -sasl
    -pop
    -imap
    -smtp
    +nntp
    +hcache
    +pgp
    +compressed
    -slang
    +curses
    +tokyocabinet -- better than default dbm for non initial loads.
    +regex


1.Why are pop/imap/smtp disabled:
    I use mutt as maildir reader and not for fetching.
2. Why is ssl/sasl disabled
    Needed only by 1. Hence disabled.

