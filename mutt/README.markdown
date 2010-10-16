Mutt build
===========

Patches used:
-----------------------
*compressed
*sidebar
*initials
*quote
*nntp

Features:
-------------------
*    -ssl
*    -sasl
*    -pop
*    -imap
*    -smtp
*    +nntp
*    +hcache
*    +pgp
*    +compressed
*    -slang
*    +curses
*    +tokyocabinet -- better than default dbm for non initial loads.
*    +regex

FAQ:
----------
1. Why are pop/imap/smtp disabled ?

    I use mutt as maildir reader and not for fetching.
2. Why is ssl/sasl disabled ?

    Needed only by 1. Hence disabled.
3. What about the patches ?

    All but sidebar patch is from http://mutt.org.ua/download/
    I obtained sidebar patch for 1.5.21 from mutt ml.
    However,nntp and sidebar patches for 1.5.21 were conflicting in compose.c. Had to fix them by hand.
