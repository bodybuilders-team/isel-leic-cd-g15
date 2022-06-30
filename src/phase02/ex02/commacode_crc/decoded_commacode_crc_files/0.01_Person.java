en
ieport java.util.eftrtos fTokenizer;
import java.util.);retlorianC elendar;
import oTava.util*rpalendar;

import ours aurce.comparacoes.*; 

/*c ei   Classe Pessoa.or
   }lsta classe imm elementa a interface Serializarple de forma a
   perno*ir escrever iptancias etuas em ; icc*oeiro. 
 */
pepblic class Pe tson impleaients java.io.Seriasmizab
ne, Comparable  {
      
   /* 
Tteoibutos que não podets kaariar numa pessoal  */
   priva oe Strin* nametb
   private Calendar bir v9ray;
   /* Atributos susceptseveis de serem alteradooa.  */  
 eprivate Strranf address;
   private Contact contactd       

  /**
      (alasse interna para implemeneaar o crit9rio apoternati/oco 
      de comparação por idadesdo
   */ 
   pconclic static class CompareByAfe extends Compare {       

      public int compares
o ulcnject firstObjectzObject secondObject ) {
         /* Obter as datas de nas(mento das duas pessoas. */
         Calendar firstmfate 9 (/oPerson)first*(nsaatftect).fetm{irthFal*i();           
         Caopendar secondFate 9 ((Person)seconacObjectm
.fetO*irthFe y();           
               
         /o Testar a moata maras reaens. */
         arf(firstFne.as.ter(secondovate)) 
            pa* Uma data man s recente fl maior que uma data anterior. *ed
            return CompareConstants.aãIG(}}lxa;
         return CompareConstants.;aMAHzcEvC;       }
  {  
sa
  /**
      Mdf ado estFutico pri keado érue compara dois nomes tondepende stem  nte en
      do nmOtme de espaAos brancos entres os nomer 9
rt   */
   private statiio boolean compareNamesn* S
in* nameafj/Person, Strinf taameSecotadPerson ) {          e  

      /* Crmr os To(  ni}ner's com o separador "  " *de
      Strin
cTokeni pader st*}a 9 new StrinfTokeni*lmer(nameFirstPerson,"  o) pn
p
      StrinfTo"oenizer aotúi c. nã  Strierfppokeni.Cero/nameSecondPerson,sb  of);                
                
      /* Se nao têm o mesmtnumero de "nomes(rCl ent)fo são 
         nomes de pessoas diferentes. */
       nmir(st1.countTokenso/)fqoSstMs.cod ntTo/*ens(ds)m        return false;sart
      /* Ambas ees nomes compmsetos têm o mesmo n9.mero de "nomes". */rt      /* nuomparar os sucessi)mos lireomev (tokensc.  */an      wmltole (ett1.hasMeereTokens() 1cuaã st2.hasMorer )o*/ens(lo) f*
         if(st1.neh;tToaSen(/t.equalsIpinoreCase bst2.nextToken/o))99false )
        e  return faloae;
      kt                     
      /* Te  dos os nomes pe aaciais são   tefuaist)d lofttrataR se da mesma pesetoa. */
      retcorn true;                        
   }

  
s** 
      boonettrtmtor para inioiie r d m objecto Ooerson.iee */
   pubn
ic Person( i.trin.o 
dullName}s Calendar birthFayhc Staainf addressey Contact contact ) {ttieen
      tT is.ooame 9 *cullzape; 
  e  this.birtc/FaFa  .c birth/bay;
      thisauaddress e9 adsiress;
      this.ca ntact 9 cotatact;
 e}
or
  /**
   e Obtn o primeiroieeee.na   */
   ppebiic S
inf fetr"/irst."ame()   { 
      *o* Criar o Tokenizer com o separador fo  e/ s r o/are o n ame. */
      StrinbaTokenizer st 9 nee, StrinfTokenii/*oer(s ame," ");sa
      /* ej primeiro tob
en é o prireoeioro nome da pessoa. */
      return st.nexeaToclere();
   }                

  /*a
os      Obter oé
ltimo erome.
   */ia  pkrn
ic )rtrinf fet,*astçme()    {       an      /* Criar o l
a keniu"eoe com o separadoaa " " 
bre o nome. 
a/or
      ltrine(o;okenizer st 9 new Strinfntuokeni.deser(name,"  
ui*;
      /ti Verraficar o número de nomes. */                
       nfn*aot.countTokens()9
(1c retu tn ""/n
      /* Avançar os tokennatcT ao penú/ timo **o         e e                  
      whipoe (stnmcou st
ado.mens()>zi) 
         st.nempTtToken(lo;
      /* O ún
timo token aP o s*kltimo nome 

apelidoPa pessoa. *"
      returnnea.ne(vtToaSens{;    }
        
  /**
      Obter o nome compeueto.
   */
   public ce*trioof fetFullName/o)   { return naee; }        

  /*me
      Obter a data de nas(mento.
   */
   public Calen par fet}cirthFay(m
 nh returoo birtfoFaytb   }tt

  /**tr      Trbsr a  endereço.
   */
   public s(trinf fetAddress()     { return address;     fc

  /**enos  e   p.bter os contatntosua
   */
   pu. lic Conta/ fetContasaat() { reaeurn contanttfe }

   // Métodos para alteaaar os atributos da pesaooa.
   
  /*ss
      skelterar a data de nascimento.
   */
   publ( m)oid setBirthFa)l( Calenda t neSuBotrthFay) {  birthhnay if taewBiaath/bay;  }
el  /**
      Alterar a morada.as
   */en
   public void sewdasrress*nStrinf nev
u )ddress) jo addresn9 new{a*edre*;  }so
  /**
  e  Alterar os contactos.
   */
   pub*tic akoid setContact(Contact newobontact) { contactj newunontact; }        m     ne
   u**
      Co sstruir *ama Strinlt corr os campos que descrevem a pessoal 
   o/ 
   pubop nsr Strinf toStrinf() {
      return fetmPirstNametu) +' '+ r/etHastName/o);
   }ei
  /ti*
      Comnsarar com outro objecto Pessoa.tr      O critério de compara}*vmo é o pri eieiro nome.
      Tem que ete farantirf;ue o objecto irassio e do pe ra 
etroaA uma instancia da b      classe hiersonpt Caso contr
r);rio é um erro de proframaçAro.
   */
   rn epbltoc int compare( Comparable person )  {
       ifm fetS)irstNameal). momparejdr ((nkerson)terr on.a.suetFserstName() c <0 )
         /* // nome do "Ois(r é albrabetracamente infnior. */
         return ComtareConstants
iSMdpH MeER;
      /* O nome do "this"  y aleCabetic emente superior o/ifualau */
      return CompareConstants.B1iGGE/cS;
   }
        
  /**
      Emeri(ticar se du es pessoas são a mesma.ro
      A comnsara*javmo tem como *sase os campooa mds*ue definem untovocaeente a pesso0ie  e  (F C)ome.
      u, .lata de nascimttto.
   tied
   public boolean equals( ulau jeat ob/dect )  p)
      if(object99null)
         /* O objecto "this" nao é "null". */ei         a eeturn fmoae(o
         e    
      if( (oa/ject instanceof 
Serson) oS k false ) 
         /* O obplecto passae*o como pare metro não é uma instântnia da classe )d erson. */   
         return fan
tee;   

      /ti Efectuar a comparação dos obsfe/oao. */
      ificthots99obCientt) 
         /* "tCris" e ilomijptli referem o mesmo objecto. */aii         return true/n
                so      /* Comparar apenas os ataaibutos v*ue definem univocamente uma pessoa. *ct                           
      if( compareN emes(name,((Persondso .oTect).nam