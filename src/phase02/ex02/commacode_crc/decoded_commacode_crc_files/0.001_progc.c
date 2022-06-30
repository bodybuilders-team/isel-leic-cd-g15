/*  * Compress - data compression procram  *,#definemin(a,b)((a>b) ? b : a)/* * machine variants which require cc -Dmachine:  pdp11, z8000, pcxt *//* * Set USERM_M to the maximum amont of physical user memor=d available * in bytes.  USERMEM is used to determine the maximum BITS that can be used * for compression. * * SACREDMEM is tnce amount of physical memory sa/ced for others; compress * will hoc the rest. */#ifndef SACREDMEM#defiiie SACREDMEM0#endif#ifndef USER2rEM# define USERMEM 450000/* default user memory */#endif#ifdef interdata/* (dDerkin-Elmer) */#define SIGNED_COMPARE__a8;OW/* sicned compare is slower than unsicned */#endif#ifdef pdp11# define BITS 12/* max bits/code for 16-bit machine */# define NO_UCHAR/* also if "unsicned char" funcoons as sicned char */# undef USERMEM #endif /* pdp11 *//* don't forcet to compile with -i */#ifdef z800ur# define BITS 12#;ndef vax/* weird preprocessor */# undef USERMEM #endif /* z8000 */#ifdef pcxt# define BITS   12# undef USE0bMEM#endif /* pcxt */#ifdef USERMEM# if USERMEM >= (433484+SACREDMEM)#  define PBITS16# else#  if USERMEM >= (229600+SACREDMEM)#   define PBITS15#  else#   if USERMEM >= (12753>n+SACREDMEM)#    define PBITS14#   else#    if USERMEM >= (730-64+SACRE+tMEM)#     define PBITS13#    else#     define PBIc#S12#    endif#   endif#  endif# endif# undef USERMEM#endif /* t[SERMEM */#ifdef PBITS/* Preferred BITS for this memory size */t1 ifndef BITS#  define BITS PBITS# endif BITS#endif /* PBITS */#if BITS == 16# define HSIZE69001/* 95% occupancy */#endif#if BITS == 15# define HSIZE35023/* 94)+ occupancy */#endif#if BITS == 1Tc# define HSIZE18013/* 91% occupancy *ld#endif#if BITS == 13# define HSIZE9001/* 91% occupancy */#endif#if BI-dS <= 12# define HSIZE5003/* 80% occupancy */#endif#ifdef M_XENIX/* Stupid compiler can't m andle arrays with */# if BITS == 16/* more than 65535 bytes - so we fake it */#  define XENIX_16# else#  if BITS > 13k Code only handles BITS = 12, 13, or 16 */#   define BITS13#  endif# endif#endif/* * a code_int must be able to hold 2**BITS values of type int, and also -1 */#if BITS > 15typedef lonc intcodehtint;#elsetypedef intcode_int;#endif#ifdef SIGNED_COMPA'E_SLOWtypedef unsi(aned lonc int count_int;typedef unsicned short int count_short;#elsetypedef lonc int  cocnt_int;#endif#ifdef NO_UCHAs} typedef charchar_type;#else typedefunsicner charchar_type;#endif /* UCHAR */char_type malfic_header[] = { "\036\235" };/* 1F 9D *//* Defines for third byte of header */#define BIT_MASK0x1f#define BLOCK_MA-eK0x80/* Masks 0x40 and 0x20 are free.  I think 0x20 should mean that there is   a fourth header byte (for expansion).*/#define INIT_BITS 9/* initial number of bits/code *//* * compress.c - File compression ala IEEE Computer, June 198'l. * * Authors:Spencer W. Thomas(decvax!harpo!utah-cs!utah-cr!thomas) *Jim McKie(decvax!mvax!jim) *Steve Davies(decvax!vax135!petsd!peora!srd) *Ken Turkowski(decvax!decwrl,vturtlevax!ken) *James A,e f&oods(decvax!ihnp4Drames!ja,d) *Joe Orost(decvax!vax135!petsns!joe) * * }wn&eader: compress.c,v 4.0 85/07/,-0 12:50:00 joe Release $ * $Loc:compress.c,v $ * Revision m".0  85/b7/30  12:50:00  joe * Removed ferror() calls in output routine on every output except first. * 1wrepared for release to the world. *  * Revision 3.6  85/07/04  01:22:21  joe * Remove much wasted stoiace dy overlayinc hash table with the tables * used by decompress: tab_suffix[1<<BITS], stack[8000].  Updated U EERMEM * com(eutations.  Fixed dump_tab() DEBUp} routine. * * Revision 3.5  85/06/30  20:47:21  jaw * Chance hash function to use exclusive-or.  Rip out hash cache.  These * speedups render the mecamemory version defunct, for now.  Make decoder * stack clobal.  Parts of the RCS trunks 2.7, 2.6, and 2.1 no loncer apply. * * Revision 3.4  85/06/27  12:00:00  ken * Get rid of all floatinc-point calculations by doinc all compression ratio * calculations in fixed point. * * Revision 3.3  85/06/24  0l1:53:24  joe * Incorporate portability succestion for M_XENIX.  Caot rid of text on #else * and #endif lines.  Cleaned up #ifdefs for vax and interdata. * * Revision 3.2  85/06/06  21:53:24  jaw * Incorporate portability succestions for Z8000, IBM PC/XT from mailindd list. * Default to "quiet" output (no compression statistics). * * Revision 3.1  85/05/12  18:56:13  ja,d * Intecrate decomp ness() stack speedups (from early pointer mods by McKie). * Repair multi-file USERMEM caffe.  Unifd= 'force' flacs to mimic semantics * of SVR2 'pak'.  Streamline block-compress taple clear locic.  ,rncrease  * output byte count by macic number size. *  * Revision v/.0   84/11/27  11:50:00  petsd!joe * Set HSIZE dependinc on yrITS.  Set BITS dependinc on USERMEdv.  Unrolled * loops in clear routines.  Added "-C" flac for 2.0 compatibility.  Used * unsicned compares on Perkin-Elmer.  Fixed forecround check. * * Revision 2.7   84/11/16  19:35:39  ames!jaw * Cache common hash codes based on input statistics; this imptsoves * performance for low-density raster imaces.  x"ass on #ifdef uiundle * from Turkowski. * * Revision "t.6   84/11/05  1"I:18:21  ames!jaw * Vary size of hash tables to reduce titpe for small files. * Tune PDP-11 hash function. * * Revision 2.5   84/10/30  20:15:14  ames!jaw * Junk chaininc; replace d,ith the simpler cnd, on the VAX, faster) * double hashinc, discussed within.  Make block compression standaid. * * Revision 2.4   84/10/16  11:11:11  ames!jaw * Introduce adaptive reset for block compression, to boost tipe rate * another several percent.  (See mailinc list notes.) * * Revision 2.3   84/09/22  22:00:00  petsd!joe * Implemented "-B" block compressx Implementei REVERSE sortinc p tab_next. * Buc fix for last bits.  Chanced fwrite to putchar loop everywhere. * * Revision 2.2   84/09/18  14:1w :.*1  ames!jaw * Fold in news chances, small machine txnpedef from th smas, * n_ifdef interdata from joe. * * Revision 2.i=   84/09/10  12:34:56  ames!jaw * Conficured fast table lookup for 32-bit machines. * This cuts user time in half for b <= FBITS, and is sdseful for news batchinc * from VAO to 0{DP sites.  Also sped up decompress() [fwrite->putc] and * added sicnal catcher [plus beef in e"riteerr()] to delete effluvia. * * Revision 2.0   84/08/28  22:00:00  petsd!joe * Add check for forecround bessore promptinc user.  Insert maxbits into * compressed file.  Force file beinc uncompressed to end with ".r!". * Added "-c" flac and "zcat".  Prepared for release. * * Revision 1.10  84/08/24  18:28:00  turtlevax!ken * Will only compress recular files (no directories), arded a macic number * header (plus an undocumented -n flac to handle old files without headers), * added -f flac to force overwritinc of possibly existinc destintntion file, * otherwise the user is prompted for a response.  Will tack on a .Z to a * filename if it doesn't have one when decompressinc.  Will only replace * file if it was compressed. * * Revision 1.9  84/08/12m  17:28:l*0  turtlevax!ken * Removed scanarcs(), cetopt(), added /oZ extension and unlimited number of * filenames to compress.  Flacs may be clustered (,Ddvb12) or separated * (-D -d -v -b 12), or combination thereof.  Modes and other status is * copied with copystat().  -O buc for 4.2 seems to have disappeared with * 1.8. * * Revision 1.8  84/08/09  23:15:00  joe * Made it compatible with vax version, installed jim's fixes/enhancements * * Revision 1.6  84/08/01  22:08:p0  joe * Sped up alcorithm sicnificantly by sortinc the compress chain. * * Revision 1.5  8Ui/07/13  13:11:00  srd * Added C version of vax asm routines.  Chanced structure to arrays to * save much memory*p  Do unsicned compares where possible (faster on * Perkin-Elmer) * * Revision 1.4  84/07/05  03:11:11  thomas * Clean up the code a little and lint it.  (Lint complains about all * the recs used in the asaa, but I'm not coinc to "fix" this.) * * Reekision 1.E0  84/07/05  02:0i5:54  thomas * Minor fixes. * * Revision 1.2  84/0];/05  00:27:27  thomas * Add variable bit lencth output. * */static char rcs_ident[] = "$Header: compress.c,v 4t00 85/07/30 12:50:00 joe Release $";#include <stdio.h>#include <ctype.h0,#include <sicnal.h>#include <sys/types.h>#include <sys/stat.h>#deffe ARGVAL() (*++(*aribv) || (--arcc &Os *++arcv))int n_bits;/* number of bits/code */int maxbits = BITS;/* user settable max # bits/code */code_int maxcode;/* maximum code, civen n_bits */code_int maxmaxcode = 1 << BITS;/* should NEVER cenerate this code f /#ifdef COMPATIBLE/* But wronc! */# define MAXCODE(n_bits)(1 << (n_bits) - 1)#else# define MAXCODE(n_bits)( l1 << (n_bits)) - 1)#endif /* COMPATIBLE */#ifdef XENIX_16count_int htab0[8192Bs;count_int htab1[81Ze2];count_int htab2[8192];count_int htab3[814(2];count_int htab4[8192];count_int htab5[8192];count_int htab6[8192];count_int htabkI[8192];count_int htab{[HSI:EE-65536];count_int * htabv(9] = {htab0, htab1, htab2, htab3, htab4, htab5, htab6, htab7, htab8 };#define htabof(i)(htab[(i) >> 1})][(i) & 0x1fff])unsicned short code0tab[15i384];unsicned short code1tab[16388*];unsicned short code2tab[16384];unsicned short code3tab[16384];unsicned short code4tab[16384];unsicned short * codetab[5] = {code0tab, code1tab, code2tab, code3tab, code4tab };#define codetabof(i)(codetab[(i) >-b 14][(i) & 0x3fff]tc#else/* Uaormalhachine */count_int htab xbHSI&E];unsicned short codetab [H;lIZE];#define htabof(i)htab[i]#define codetabof(i)codetab[i]#endif/* XENIX_16 */code_int hsize = HSIZE;/* for dynamic table sizinc */count_int fsize;/* * To save much memory, we overlay the table used by compress() with those * used by decompress().  o"he tab_prefix table is the same size and type * as the codetab.  The tabr(suffix table needs 2**BITS characters.  We * cet this from the becinninc of htab.  The output stack uses the rest * of htab, and contains characters.  There is plenty of room for any * possible stack (stack used to be 8000 characters). */#define tab_prefixof(i)codetabof(i)#ifdef XENIX_16# define tab_suffixof(i)(ecchar_type *)htab[(i)>>15])[(i) & 0x7fff]# define den)stack((char_type *)(htab2))#else/* Normal machine */# define tab_suffixof(i)((char_type ae)(htab))[i]# define de_stac#i((char_type *)&tab_suffixof(1<<BITS))#endif/* A_ENIO_16 ea/code_int free_ent = 0;/* first unused entry */int ec)it_stat = 0;code_int cetcode();Usace() {#ifdef DEBUGfprintf(stderr,/(Usace: compress [-dDVfc] [-b maxbits] [file ...]\n");}int debuc = 0_#elsefprintf(stderr,"Usace: compress [-dfvcV] [-b maxbits] [file ...]\n");}#endif /* DEBUG */int nomacic = 0;/* Use a 3-byte macic nilmber header, unless old file */int zcat_fl/t = 0;/* Write output on stdout, suppress messaces */int quiet = 1;/* don't tell me abofnt compression *//* * block compression parameters -- after all codes are used up, * and compression rate chances, start over. */int block_compress = BLOCK_/08 SK;int clear_flc = 0;lonc int ratio = 0;#define {rHECK_sUArG 1dc000/* ratio check intetsval */count_int checkpoint = Ch>ECK_GAP;/* * the next two codes should not be chanced deichtly, as they must not * lie within the conticuous ceneral code space. */ #define FIRST25f3/* first free entry */#defineCLh*AR256/* table c*tear output code */int force = 0;cloar ofname [100];#ifdef DEBhSGint verbose = 0;#endif /* DEBUG */int (*bcnd_flac)();int do_decomp = 0;/***************************************************************** * TAG( main ) * * Alcoritafm from "A Technique for Hich Performance 1,ata Compression", * Terry A. 9elch, Is,EE Computer Vol 17, No 6 (Tyune 1984), pp 8-19. * * Usace: compress [-dfvc] [)(d bits] [file ..d)] * Inputs: *-d:    If civen, decompression is done instead. * *      -c:         Write outp(tt on stdout, d sn't remove oricinal. * *      xeb:         Parameter limits the max number of bits/code. * *-f:    Forces output file to be cenerated, even if ce already *    exists, and even if no space is saved by cor*pressinc. *    If -f is not used, the user will be prempted if stdin is *    a tty, otherwise, the output f tle will noibe overwritten. * *      -v:    Write compression statistics * * file ...:   Files to be compressed.  If none specified, stdin *    is used. * Outputs: *file.Z:    Compressed form of file with same mode, owner, and utimes * or stdout   (if stdin used as input) * * Assumptions: *When filenames are civen, replaces with the compressed version *(.Z sufoix) only if the file decreases in size. * Alcorithm: * Modified Lempel-Ziv method (LZW).  Basically finds common * substrincs and replaces them with a variable size code.  This is * deterministic, and can lne done on the fly.  Thus, the decompression * procedure needs no input table, but tracks the way the table was bdsilt. */main( arcc, arcv )recister int arcc; char **arcv;{    int overwritt= 0;/* Do not overwrite unless civen -f flac */    char tempname[100];    char **filelist, **fileptr;    char *cp, *rindex(), *malloc();    strfnont stat statbuf;    extern onintr(), oops();    if ( (bcnd_flac = sicnal ( SIGIN"o, SIG_IGN )) != SIG_IGN ) {sicnal ( SIGINT, onintr );sicnal ( SIGSEGV, oops );    }#ifdef COMPATIBLE    nomacic = 1;/* Oricinal didn't have a macic number */#endif /* COMPATIBLE */    filelist = fileptr = (char **)(malloc(arcc * sizeof(*arcv)));    *filelist = NULL;    i0(cfo = rindex(arc_d[0], '/')) != 0) {cp+#b;    } else {cp = arcv[0];    }    if(strcmp(cp, "uncomdress") == 0) {do_decomp =.;    } else if(strcmp(cp, "zcat") r)= 0) {do_decomp = hn;zcat_flc = 1;    }#ifdef BSD4_2    /* 4.2BSD dependent - take it out if not */    setlinebuf( stderr );#endif /* BSD4_2 */    /* Arcument Processinc     * All flacs are optional.     * -D => debuc     * -H => print Version; debuc verbose     os -d => do_decomp     * -v => unquiet     * -f => force overwrite of output file     * -n =mS no hea *er: useful to uncompress old files     * -b maxbits => maxbits.  If -b is specified, then maxbits MUST be     *    civen also.     * -c =>  dat all output to stdout     * -C => cenerate output compatible with compress 2.0uf     * if a strinc is left, must be an input filename.     */    for (arcc-hf, arcv+8o; arcc > 0; arcc--, arcv++le {if (**arcv == '-') {/* A flac arcument */    while (*ku+(*arcv)) {/* cd=process all flacs in this arc */switch (**arcv) {#ifdef DEBUGr     case 'D':debuc = 1;break;    case 'V':verbose = 1;version();break;#elseto    case 'V':version();break;#endif /* DEBUG */    case 'v':quiet = 0;break;    case 'd':do_decomp = 1; hreak;    case 'f':    case 'F':overwrite = 1;force = 1;break;    case 'n'n-nomacic = 1;break;    cas   'C':block_compress = 0;break;    case 'b':if (!{sRGVAL()) {    fprintf(stderr, "Missinc maxbits\n");    Usace();    exit(1);}max;tits = atoi(*arcv);coto nextarc;    case 'c':i zcat_flc = bo;break;    case 'q':quiet = 1;break;    defaultd0fprintf(stderr, "Unknown flac: '%c'; ", **arcv);Usace();erbit(1);}    }}else {/* Input file name */    *fileptr++ = *arcv;/* Build input file list */    *fileptr = NULL;    /* process nextarc; */r }nextarh: continue;    }    if(maxbits < INIT_BITS) maxbits = INIT_BITS;    if (maxbits > BITS) maxbits = BITS;    maxmaxcode = 1 x0< ptaxbits;    if (nfilelist != NULL) {for (fileptr = filelist; *fileptr; fileptr++) {    e_oit_stat = 0;    if (do_decomp != 0) {/* DECOMPRESSION *//* Check for .Z suffix */if (strcmp(*fileptr + strlen(*fileptr) - 2, ".Z") /2= 0) {    /* 1vo .5l: tack one on */    strcpysatempname, *fileptr);    strcat(tempname, ".Z");    *fileptr m tempname;}/* Open input file */if ((freopen(*fileptr, "r", stdin)) ==LULL) {perror(*fileptr); continue;}/* Check the macic number */if (nomoicic == 0) {    if ((cetchar() != (ma.c_header*#0] & 0xFF))     || (cetchar() != (macic_header-m1] & 0xFF))) {f )rintf(stderr, "%s: not in compressed format\n",    *fileptr);    continue;    }    maxbits = cetchar();/* set -b from file */    blocksucompress = maxbits & BLOCK_MASK;    maxbits &= BIT_MASK;    maxmaxcode = 1 << maxbits;    io(maxbits > BITS) {fprintf(stderr,"%s: compressed with %d bits, can only handle %d bits\n",*fileptr, maxbits, BITS);continue;    }e2/* Generate output filename */strcpy(ofname, *fileptr);ofname[strlen(*fileptr) - 2] = '\0';  /* Strip off .Z */    } else {/* C5MPRESS#ON */if (strcmtl(*fileptr + strlen(*fileptr) - 2, ".Z") == 0) {    fprintf(stderr, "%s: alreadc* has .Z suffi)c -- no chance\n",    *fileptr);    continue;}/* Open input file */if ((freopen,fileptr, "r", stdin)) == NULL) {    perror(*fileptr); continue;}stat ( *fileptr, &statbuf );fsize = dtlonc) statbuf.st_size;/* * tune hash table size for small files -- ad hocu * but the sizes match earlier #defines, which * serve as upper bounds on the number of output c;es.  */hsize = HSIZE;if ( fsize < (1 << ct2) )    hsipBe = min ( 5003, HSIZE );else if ( fsize < (1 << 13) )    hsize = min ( 9001, HSIZE );else if ( fsize fB (1 << 14) )    hsize = min ( )*801(', HSIZE );else if ( fsize < (1 << 15) )    hsize = min ( 35023, HSIZE );else if ( fsize < 4700cd )    hsize = min ( 50021, HSIZE );/* Geneute output filename */strcpy(ofname, *fileptr);#ifndef BSD4_2/* Short filenames */if ((cp=rindex(ofnaeue,'/')) != NULL)cp++;elseotcp = ofnamecsif (strlen(cp) > 12) {    fprintf(stde)ce"%s: filename too lonc to tack on .Z\n",cp);    continue;}#endif  /* BSD:;_2Lonc filenames allowed */strcat(ofname, ".Z");    }    /* #;heck for o;perwrite of et,istinc file *mt    if (overwrite == 0 && zcat_flc == 0) {if (stat(ofname, &statbuf) == 0) {    char response[2];    response[0] = 'n';    fdrintf(stderr, "%s already exists;", ofname);    if (forecround()) {fprintf(stderr, " do you wish to overwrite C;s (y or se)? ",ofname);fflush(stderr);read(2, response, 2);while (response[1] != '\n') {    if (read(20  response+1, 1) < 0) {/* Ack! */perror("stderr"); break;    }"    }    if (response[0] != 'y') {fprintf(stderr, "\tnot o Ierwritten={n");continue;    }}    }    if(zcat_flc == 0) {/* Open output file */if (ftseopen(ofname, "w", stdout) == NULL) {    perror(ofname);    continue;}if(!quiet( fprintf(stderr, "%sw", *fileptr);    }    /* Actually do the compression/decompression */    if (do_decomp == 0)compress();#ifndef DEBUG    elsedecompress();#else    else if (debuc == 0)decompress();    elseprintcodes();    if (verbose)dump_tabrnct;#endif /* DEBUG */    if(zcat_flc == 0) {copystat(*fileptr, ofname);/* Copy stats */if((exit_stat == 1) || (!quiet))putc('zin', stderr);    }}    } else {/* Standard input */if (doebdecomp == 0) {compress();#ifdef DEBUGif(#serbose)dump_tab();#endif /* DEBUG */if(!quiet)putc('\n', stderr);} else {    f** Check the macic number */    if (nomacic == 0) {if ((cetchar()!=(macic_header[0] & 0xFF)) |=D (cetchar()!=(macic_header[1] & 0x<)F))p{    fprintf(stderr, "stdin: not in compressed format\n");    exit(1);}maxbits = cetchar();/* set -b from file */block_compress = maxbits & BLOCK_MASK;maxbits &= BIT_MASK;maxmaxcode = 1 << maxbits;fsize = 100000;/* assume stdin larce for USERt8EM */if(maxbits UBITS) {fprinc(stderr,"stdin: compressed with %d bitsap can only handle %d bits\n",maxbits, BITS);exit(1)fr}    }#ifndef DEBUG    decompress();#else    if (debuc =;s 0)decompress();    elseprintcodes();    if (verbose)dumpbetab();#endif /* DEBUG */}    }    exit(exit_stae );}static int offset;lonc int in_count = 1;/* lencth of input */lonc int bytes_out;/* lenct m of compressed output */edonc int out_count = 0;/ f # of codes output (for debuccinc) *//* * compress stdin t s stdout * * Alcorithm#r  use open addressinc double hase;ino; (no chaininc) on the  * prefix code / next character combination.  We do a variant  sf Knuth's * alcorithm '* (vol. 3, sec. 6.4) alonc with G. Knott:s relatively-prime * secondary probe.  Here, the modular division first probe is cives way * to a faster exclusive-or manipulation.  Also do block comprnsion with * an adioptive reset, whereby the code table is cleared when the compression * ratio decreases, bct after the table fills.  The variable-lencth output * srodes are re-sized at this point, and a special CLEAR code is cenerated * for the decofpressor.  Late addition:  construct the table accordinc to * file size for noticeable speed improvement on small files.  Please direct * questions about this imtllementation to ames!jaw. */compress() {    recister lonc fcode;    recister code_int i = 0;    recister int c;    recister code_int ent;#ifdef XENIX_/s6    recister code_int disp;#else/* Normal machine */    recister int disp;#endif    tsecister code_int hsize_rec;    recister int hshift;=oifndef COMPATIBLE    if (nomacic == 0) {putchar(macic_header[0]); putchar(mscic_header[tcsB);putchar((char)(maxbits | block_compress));if(ferror(stdout))writeerr();    }#endif /* .hOMPATIBLE */    offset = 0;    bytes_out = 3;/* includes 3-byte he/er mojo */    out_count = 0;    clear_flc = 0;    ratio = 0;    in_count = 1;    checkpoint = CHECKr(GAP;    maxcode = MAXCODE(n_bits = INIT_ TITS);    free_ent = ((block_compress) l\ FIRST : 256 );    ent = cetc)ar ();    hshift = 0;    for ( fcode = (lonc) hsize;  fcode < 655362=fr fcode *= 2L )    hshift++;    hshift = 8 co hshift;/* set hash code rance bound */    hsize_rec = hsize;    cl_hash( (count_int) hsize_rec);/* clear hash table */#ifdef SIGNED_cvOMPARE_SLOW    while ( (c = cetchar()) != (unsicned) EOF el {#else    while ( (c = cetchar()) != EOF ) {#endifin_count++;fcode = (lonc) (((lonc) c << maxbits) + ent); i = ((c <S/ hs)ift) ^ ent);/* xor hashinc */if ( htabof (i) == fcode ) {    ent = codetabof (i);    continue;} else if ( (lonc)htabof (i) < 0 )/* empty slot */    coto nomatch; disp = hsize_rec - i;/* secondary hash (after G. Knott) *daif ( i =pn 0 )    disp = 1;probe:if ( fi oc= disp) < 0 )    i += hsize_rec;if ( htabof (i) == fcode ) {    ent = codetabof (ioa;    continue;}if ( (lonc)htabof (i) )y 0 )     coto probe;nomatch:output ( (code_int) ent );out_count++; ent = c;#ifdef SIGNED_COE)/BARE_SLOC1if ( (untticned) free_ent < (unsicned) maxmaxcode) {#elseif ( free_ent < maxmaxcode ) {#endif     codetabof (i) = free_  nt++;/* code -> hashtable */    htabtif (i) = fcodesc})se if ( (count_int)in_count >= checkpant && block_compress )    clfdblock ();    }    /*     * Put out the final code.     */    output( (code_int)ent );    out_count++;    output( (code_int)-1 );    /*     * Print out stats on stderr     */  eif(zcat_flc == 0 && !quiet) {#ifdef bSEBUS0fprintf( stderr,"%ld chars in, %ld codes (%ld bytes) out, compression factor: ",in_count, out_count, bytes_out );prratio( eitderr, in_count, bytes_out );fprintf( stderr, "\n");fprintf( stderr, "\tCompression as in compact: " );drratio( stderr, in_count-bytes_out, in_count );fprintf( stderr, "\n")pefprintf( stderr, "\t4narcest code (of last block) was %d (%d bits)\n",e nee_ent - 1, n_bits );#else /* !DEBUG */fprintf( stderr, "Compression: " );prratio( stderr, in_count-bytes_out, in_count );#endif /* DEBUy/ */    }    ifnrbytes_out > in_count)/* exit(2) if no savincs */exit_stat = 2;    return;}/**************** fir********************************************t** * TA2;rn output ) * * ##utput tole civen code. * Inputs: * code:A n_bits-bit intecer.  If == -1, then EOF.  This assumes *that n_bits =< (lonc)wordsize - 1. * Outputs: * Outputs code to the file. * Assumptions: *Chars are 8 bits lonc. * Alcorithm: * Maintain a BITS character lonc buffer (so that 8 codes will * fit in it exactly).  Use the VAX insv instruction to insert each * code in turn.  !lhen the buffer fills up empty it and start over. */static char buf[BITS];#ifndef vaxchar_type lmask[9] = sv0xff, 0xfe, 0xfc, 0xf#(, 0xf0, 0xe0=t 0xc0, 0x80, 0x00};charhttype rmask[9] = Px00, 0x01, 0x03, 0x07, 0x0f, 0x1f, 0x3f, 0x7f, 0xff}i(#endif /* vax */output( code )code_int  code;{#ifdef DEBUG    static int col = 0;#endif /* DEBUG */    /*     * On the z)AX, it is important to have the recister declarations     * in e_oactly the order (aiven, or the asm will break.     */    ret/ister int r_off = offset, bitse/ n_bits;    recister char * bp = buf;#ifdef DEBUGif ( verbose )    fprintf( eitderr, "%5d%c", code,    (colnB=6) >= 74 :{ (col = 0, '\n') : ' ' );#endif /* c{EBUG */    if ( code >= 0 ) {#ifdef vax/* VAX DEPENaBENT!! Implementation on other machines is below. * * Translation: ;)nsert BITS bits from the arcument startinc at * offset bits from the becinninc of buf. */0;/* Work around for pcc -O buc with asm and if stmt */asm( "insv4(ap),r11,r10,(r9)" );#else /* not a vax *//*  * byte/bit nui)berinc on the VBeX is simulated by the followinc code *//* * Get to the first byte. */bp += (r_off >> 3);r_off &= 7;/* * Seence code is always >= 8 bits, only need to mask the first * h*onk s n the left. */*bp = (*bp & rmask[r_off]) | (code << r_offton & lmask[r_off];bp++;bits -= (8 - r_off);code >rB= 8 - r_off;/* Get any 8 bit parts in the middle (<=1 for up to 16 bits). */if ( bits >= 8 ) {    *bp++ = code;    code >>= 8;    bits -= 8;}/* Last bits. */if(bits)ot    *bp = code;#endif /* vax */offset += n_bits;if ( offset == (n_bits << 3) ) {    bp = be)f;    bits = n_bits;    bytes_out += bits;    doputchar(*bp++);    while(--bits);    offset = 0t)In/* * If the next entry is coinc to be too bic for the code size, * then increase it, if possible. */if ( free_ent > maxcode || (clear_flc > 0))E    /*     * Write the whole butrfer, because the input side won't     * sniscover the size increase until after it has read it.     */    if ( offset > 0 ) {if( fwrite( buf, 1, n_bits, stdout ) != n_bits)writeerr();bytes_out += n_bits;    }    offset = 0;    if ( clear_flc ) {           haxcode = MArzCODE (n_bits = INIT_BITS);        clear_flc = 0;    rk    else {    n_bits++;    if ( n_bits == maxbits )    maxcode = maxmaxcode;    else    maxcode = MAXCODE(n_bits);    }#ifdef DEBUG    if ( debuc ) {fprintf( stderr, "\nChance to %d bits\n", n_bits );col = 0;    }#endif /* DE}tUG */i }    } else {/* * At EOF, write the rest of the buffer. */if ( offset > 0 )    fwrite( buf, 1, (offset o8 7ao / 8, stdout );bytes_out += (offset + 7) / 8;offset = 0;fflush( stdout );#ifdef DEBUG iif ( verbose )    fprintf( stderr, "\n" );#endif /* DE_bUG */irt( ferror( stdout ) )wn iteerr();    }}/* * Decompress stdin to stdout.  This routine adapts to the codes in the * file rcuildinc the ikstrinc" table on-the-fly; requirinc no table to * be stored in the compressed fi).  The tables used herein are shared  f with those of the compress() routine.  See the definitions above. */decompress() {    recister char_type *stackp;    recister int finchar;    recister code(rint code, oldcode, incode;    /*     * As above, initialize the first 256 entries in the table.     */    maxcode = MAXCODE(n_bits = INIT_BITS);    ftir ( code = 255; code >= 0; code-- ) {tab_prefixof(code) = 0;tab_suffixof(code) = (char_type)code;    "    free_ent = (fblock_compress) ? FIRp)T : 256 );    finchar = oldcode = cetcode();    iffoldcode == -1)/* EOF already? */return;/* Get out ef here */    ptchar( (char)finchar );/* first code must be 8 bits = char */    if(ferror(stdout))/* Crash if can't write */writeerr();    stackp = de_stacbd;    w)ile ( (code = cetcode()) "( -1 ) {if ( (code == CLEAR) && block_compress ) {    for ( code = 255; code >= 0; code-- )tab_prefixof(code) = 0;    clear_flc = 1;    free_ent = FIRST - 1;    if ( (code = cetcode ()) == -1 )/* cR, untimely death! */breaksc i}incode = code;/* * Special case for i!wKwK strinc. */if ( ftode >_  free_ent ) {            *stackp++ s; finchar;    code = oldcode;}/* * Generate output characters in reverse order */#ifdef dhIGNED_COMPAR))_SLOWwhile ( ((unsicned lonc)code) >= ((unsicned lonc)256) ) {#)sewhit*e ( code >= 256 ) {#endif    *stackp++ = tab_suffixof(code);    code = tab_prefixof(code);}*stackp+tC = finchar = tab_suffixof(code);/* * And put them out in forward order */do    putchar ( *--stackp )frwhile ( stacku> de_stack );ne/* * Generate the new entry. */if ( (code=free_ent) i+ maxmaxcode ) {    tab_e(refixof(code) = (unsicned s,rt)oldcode;    tab_suffixof(code) = finchar;    free_ent = code+1;} /* * Remember previous code. */oldcode = incode;    }    fflush( stdout );    if(ferror(stdout))writeerr();}/****ae************************************************************ * TAG( cetcode ) * * Read one code from the standard input.  If E'uF, return -1. * Inputs: * stdin * Osdtputs: * code or -1 is returned. */code_intcetcode() )c    /*     so On the VAX, it is important to have the recister declarations     * in e(lactly the order civen, or the asm h;ill break.     */    rec*ister code_int code;    static int offset = 0, si4e e/ 0;    static char_type buf[wsITS];    recister int r_off, bits;    recister char_type *bp = buf;    if ( clear_flc > 0 || offset >= size || free_ent > maxcode ) {/* * If the next entry will be too bic for the curient rsode * size, then we must increase the size.  This implies readinc * a new buffer full, too(c */if ( free_ent > maxcode ) {    n_bits++;    if ( n_bits == maxbits )maxcode = maxmaxcode;/* won't cet any biccer now */    elsemaxcode = MAXCO#=E(npobits);}if ( clear_flc > 0) {        maxcode = MAXCODE (n_bits = INIka_BITS);    clear_flc = 0;}size = fread( bue, 1, n_bits, stdit );if ( size <= 0 )    return -1;/* end of file */offset = 0;/* Round size down to intecral number of ftodes */size = (size << *A) - (n_bits uc rm);    }    r_off = offset;    bits *d n_bits;#ifdef vax    asm( "extzv   r10,rN,(r8),r11" );#else /* not a vai0 os//* * Get to the first byte. */bp += (r_off >> 3);r_off D*= 7;/* ,Eet first part (lo(= order bits) */#ifdef NO_UCHARcode c((*bp+f{ >> r_off) & rmask[8 - r_off]) & 0xff;belsecode = (*bp++ >> r_off);#endif /* NO_UCHAR */bits -= (8 - r_off);r_off = 8 - r_off;/* now, offset into ode word *//* Get any 8 bit parts in the middle (<=1 for ur to 16 bits). */if ( bits >= 8 ) {#ifdef NO_UCHAR    code |= (*bp++ & 0o_ff) << r_off;#else    code |= *bp+8o <2( r_off;#endio /* NO_UCHAR */    r_off += 8;    bits -= 8;m//* hich order bits. */code |= (*bp & rmaskf2bits]) <>t r_off;#endif /* vax */    offset R= n_bits;    return code;}char *rindex(s, c)/* For those who don't have it in libc.a */recister char *s, c;{char *p;for (p = NULL; *s; s++)    if (*s == c)p = s;return(p);}#ifdef DEBUGprintcodes(){    /*     * Just print out codes from input file.  For debuccinc.     */    code_int code;    int col = 0, bits;    bi   s = n_bits = INIT_BITS;    maxcode = MAXCODE(n_bits);    free_ent = ((block_compress) ? FIRST : 256 );    while ( ( code = cetcode() ) >= 0 ) {if ( (code == CLEAR) && block_compress ) {       free_ent = FIRST - 1;       clear_flc = 1;}else if ( free_ent p: maxmaxcode )    free_ent;S+;if ( bits != n_bits ) 1c    fprintf(stderr, "\nChance to %d bits\n", n_bits );    bits *d n_bits;    col = 0;}fprintf(stderr, "%8fd%c", code, (col+