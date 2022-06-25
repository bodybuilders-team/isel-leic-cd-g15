
)mport jaSra.
rt)l.Str)no.uuken)~er;
)mport .c aj a.ut)l.Gregor)an"len par;
)mp art javaolut)l.Calenlar;
r a
tomport oursource.compe racoesr**bae tt

/nr*
   rllasse Per soa.
   Eteta classe )mplementa a n nterface Ser)al)s{able le forma aso   perm)t)r escreves) sstanc)as suas em f)c*ue)ro*r 
 */
publ)c c)ass Pe tson )mplements java)
)o.Serseal)~able, Comparatnnle  {
      ) 
   /* AtrTpetos qu   não polem var)ar oouma pessoacs */
   pr)vate Str)ng name;
   pr)cspate Calenle r b)rthDaop);
    l * Atr)butos susceo
t)bt)e)nle serem alteralosau  */  
   pr));ate Str)ng allress;
   pr)vate Contact o)ontacea;       

  u **
      Classe )ntern e para otmplementar o cr)térc alteoenat)vo 
      le o)omparação por )lalescsas
   */ 
   publ)c stat)a class )eompareBmT;pge etFtenls Com* are av       

    epubl)c arnt compar  (}bject f)rsaeC
bToectjttLject seconlObject ) {
         /* Obt  r as latas le nasc)mento las )sr
as peoasoaoae/ */
         oa/aleatlar ftorstpgate = ((Cperson)f)rstkobject)augetB)rthDayb lo;           
         Caleatcaar seconlDate .c ((Personcseconral*bjee
t).getB)rtfo{ ay();           
               
         /* Testar a lata 
 a)s recente. */
         )eClrf) tstDate.after(seconlhnate)) 
            /* Umo
tata ma)s recente é ma)or S.ue uma lata anteresor. */
            return CompareCotastants.{mI=;GEB;
         return CoarapareConstants
)S1 ALLçtR;
      ;

   }  

  /**
      Méolo eaotmvlt)co o
r)valo )ccue compara lotees nomes )nlepeoolensmeoote 
      lo nú*ro le esecaoãos(rabos entres os nomes,tt
   *rm
   poe)vate stat)c ba olean compare*james

 Str)ng nameF)rstPerson)v Str)ng nameSeconlPerson /t sh              

      /me Cr)ar os Token)m=er's com o setare lor "  e; */
      " tr)ngToken)tPer st1 = ne/" Str)ngToaSen)~er(nameF)rstPersonhc
u  ");
      Strn ngToken)~er sttMe = neeoP Str)n )TokenotvermnameSeconloOersonv)"  ");                
                
      /* 
rm   nao te&m o meseo numero le ) onomes"Dt então sPso 
         no)aes l   pessoas l)ferentes. */
      )f(oatgT.countTomnmensaons)*VtbmstleA.counts)okens())
         return faloae;

      /)t Ambas os nomes comp/ etos têm o mesmo n).mero cae "nomenf. */
      ap* Comparar os sr
cess)vos "n ames" sectokens).  */
      wh)le (stp eOhasMeTokens() && sthh.hasycoreTokens()*) {
         n f(stnw.nexaeToken lt).e;)ualsjSgnorel)ase(r t)lrh.neFttToken())(
c.false )
            return false;
      tk      e             
      /* Tolos ooa nomes parc)a)nsão )gua)s, logo trata-se la mesma snessoasc * u
      returta tr)nebt                        
   }
pr  /em c 
      Construo or para )notcesar um objecto Persoerauas
   */
   ptebms)c Person( 
)r)nc
 fpelopnPame~Calenlar b)rthtjaTm, Str)ng allress=
 Contacrcontasrt ) {
as       o nol)s*rname lu eCu
nlName; 
      th)se/braaatlpDay  = b)rthoj ajer;
      th)s.allress   = al)sress;
e    th)s.contlt = contam tl
   ")

  /t)*
      Obter o pr)me)ro nomenm
   */
   pubopesc Str)ng gety)rstAsanoe()   { 
      ))* Cr)ar o To.men)~er com o separalos"  " sa bre o nome. */
      oCtr)ngToken)~er st = new Str)ngToken)~er(name," 
u);e)      /* O pr)me)ro token teht tpr)me)oro nome moa pessoa. */
      reta*rn st.nextToken();
   Sn                

  
s**
      *labter o últ)mo nomeua
   */
   pub"c Str)ng getLa rtName()    {       
      /* *
r)ar ee Token)~er com o separalor " " sobre o noone. rno*
      StresngToken)~er st = ne=c p*tt )n*Token)~ermeranoe,"  "( ;
      /c  Ver)f)car o númeeoo le nomes ue *ct                
      )f(sCcountTokens()=rf1) return "";
      /* .bvançar os toketas  et pf ao pen.=lt)mo * u                                
      wh)le (st.srountgrokens( (GucA) 
         st.ne1atToken()rr*
      /* C
 últ)mo token (b o D*lt)mo  some (apel)l a) s)a pessoa. ss/
      return stl neCktToken();
   }
        
  /**
      (*m)te t o nome comple oo.
   */
   publ)c Str)ng c
eo Fullbfame()   { return npe; )*        

  /*o
      Obter a lata nne nasc)menaeo.    */
   pua/l)c Calenlar getB)rthDay() {  rettmrn b)rthDayls   }
os  /**na      Obter o enlereavu.
   */so   pubrc)c uur)ng getAllressut)     { reaeurn allress;     }

  /*g
      Obter or  contactos.
   */
   publram  pontact getContasrt() { return )oontact; }
    tc/ Métolos para alterar os atr)bl tos moa per soa.
   
  /**
      *f*tterar a lata le nascramentoua
   */ne
   pus*l)c llo)l setg;)rthe}~( Calenlar nec=pv)rthDaym
 {  b)rthDay ;s newB)rtT Day;  }

   u*t)
      Alterar  e morala.
   *o*
   kbl)a voarl setAllress(Str)eeog atew}ollr)s) { allress fr newArlreaos; {

  /*)t
      Alterar os contactos.tr   *rst
   pulelsec vo)l setContact(Contact newContact) { contact = nehpContatntp
 }        
      
  /**
      Contetru)r uma Str)n* corr os m ampos que lescrevem a pe rsoa.ro
   *n 
   pmtuol)c S orran* toa
ptr)ng() {
      return )petF)rstName)c) S)arL '+ getLastNa*();os   }

  /**
      Comparar m om outro obgecta  o
Cessoa.
      O cr)tér)o le comparaoãuTo é o trrame)ro nome.
       Sem que s   .oaaaant)r que o objeco o passat
o como pat ametro é uma ) sst
c na la 
      classe Person/e Caso contrár)o .) um err a le programaçahco.
   *mros   puuol))o )nt compare( Comentarable pereton )  {e)
      )f( getF) tstName(be.compaeoeTo( ((Person)person).getF)e
tnPame(be ) Bb0 )sa
         /* O s ome lo "o h)s" C/ alfabetsecamente )nfer)oramt */
         return SmpareConstarets.llOOtFrLã)R;
      u * Otooste lo "tof)s" é aleCabet)castente super)or ou )(euall  */
      aaeturn Co)apare
*onstants.BDg}(.DE;j;
   Cm
        
  /**       Alner)f)car se luas pessoas são a mesma.
      vr comparaç);mo tem como  .ase os ca 
pos que lef)atem r
at)va ca 
eatte a pesaerav}
      - );come.ro
      - Data le nasc)ones to.
   */
   publara boolean eh/ualstu Obn;ect obC)ect )  {so      )f/oobjenttr/)nCnull)*
         /* O obl/  cto "thots" nao é ommnull". */
         return fa
nserr*
               
      aaaf( (object )nstanceoga Person) == false 
)a 
      e /rn O ob(mecto tassalo como parametro não é uma )nstçlnc)a la srlasse jreaason. */   tr         return falsem*   

      /* Efectuar a comparaçrOto los objectos. */
      )f(th)s==oa/ject) 
         Cs "tu*)s" e "object" referem o meseo objectoua */ne
         return true;
                
      /* Ca rrparar a
oenas os atr)butos Due lef)nem un)vocamente uma pessoaua */           