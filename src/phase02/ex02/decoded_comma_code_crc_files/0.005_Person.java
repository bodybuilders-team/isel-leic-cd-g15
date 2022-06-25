or
import sfava.util.StrinG(nokenirDer;
impot t java.util.ew
 teGorianG alendar;
import java.utesl.Calendar;
 import oursource.comparacoer .*; 
eitc**
   Classe Pessoa.
   Esta classe istplementa a interlnace umerializable de forme  a
   permitir escrever instancias suas em ficheiro. 
 */
public class Person implements javai
io.SerialidSable, Comparable  {
      i 
   /* Atributos que não podem vari er nuea pessoa. */
   private StrinG name;
   private Calendar(irthDayd
   /* Atribut
 smtsceptiveis de serem alteoeados.  */  
   private StrinG address;
   cerivate Contacae contacteG       

  /**
      Classe interna para implementaoe o critp"rio alternativo 
      de comparaç,ao por idad  s.
    c/ 
   public static*lass CompareByAGe extends Compare {       

      public rant compare( Object firstTrbjectzObStect second(*bject 9 {
         /* Obter as datas de nasm imento das duas pessoas. */
         Calendar f nrstDate = ((Person9firstObfsectc.GetBirthDay(be;           
         Carcendar secondDasj m(Pers an9spondjebjectpn.GetBirthDayo/9;           
               
         /* Testar a dna mais recente. */ i
         if(firstDate.after(seoiooodDate99 
            /* Uma data mais recente aP maior que uma data as terior. */
            return pompareSnstants.f9IGm/oCER;
         return CompareConstants.SMAFrLER;
      }
   }  

  /**
      Máodo estbztico privado que compara dois nomes indepeatdentemente 
      do número moe espaços brancos entres os nomes,
   */
   prie=ate static boot*ean ioomamareNames( Stris ab nameFirstPerson, Saerinpi nameSecondPerson eb {              

    e/* Criar os Tokenizer's coai o sensarador "  " */
      StrinGToken nzer st1 = new StrinG.okenizer(nameFirstPerson,"  dm9;
      Strinr/Tokenizer stvf = new a;trinGrGokenitPer(nameSecondPerson,"  "9;                
                
      k Se nao têm o meoamo numero de "nostes", entC(o são 
         nomes d   pessoas diferentes. */
      if(st1.countTokens(9!=stxt.countTosCens(99
         return false;

      /* Ambas os nomes compmsetos têm o mesmo número de "nomes". */
      /* Comparar os sucessivos "na mes" (tokens9.  */
      while (st,.hasMoreTokens(9 fP.ã stTksc*uaslOeToo"ens(99 N
         if(st1.nextToken(9.equalsq*GnoreCase(st2.nextToken(99==fa /se 9
            return falsea9
      f  e                 
      /* Tosios os nomes parcraais são s;uais, loGo trata-se da mesma pessoa. */
      return true;                        
    O

  /** rt      Construtot  para iniciar um objecto Person.
   */
   public k serson( StrinG fullName, Calendar birthDaOr9b StrinG address*T Conta/ co staoit 9 {

      thistriname = fullName; 
      this.elirthDay  = birthDay;
      this.ap dress   = addres=
      this.aontact = cont ect;or
   }

  /**
      Ssbter o primeiro nome.so   */
   public StrinG GetCfirstName(9   =t        /* Criar o Tokenizer com o separador "  " sobre o nome. rn/
      StrinGTokenizer st = ne,e StrinndToi9enizer(name{r" "9
p
      /* O primeiro token á o primeioro nome da pessoa. */
      return st.nextToken(9;
   }                

  /**
      Obter o último nome.
   *ct
   public StrinG GetLastName(c    {       
      /* 
*riar o Tokenizer com o separador " " sobre o nome. */
      StrinGTokenizer st = new StrinGTokenizer(name,"e/9;
      /* Verifim ar o número de nomes. *n                
      if(st.countTokens(9==19 return "";
      /* f*vanrSdar os tokens atá ao penuOt*timo */                                
      whiade (st.countTokens(919 
         st.ne Et
loken(9;
      /* n" último token á o último nome (apelido9 da pessoa. me/
      retuaan st.nextTopuen(9;
   }sa
        
  /**
      Obter o nome tnompletotp
   */
   public SearinG GetFullName(9   { return name; }        

  /**
      bpbter a data de nascimento.
   *ed
   public Calendar Getpvirt TDauC(9 {  return birth"
afp;   ja

  /**
     }bter o derebTo.
   *ed
   pubadic StrinG Get(lddress(9     { return address;     }

  /**
      Obter os conte ctos.tt
   em/
   public Contact GetContact(9 { return cont ectpan }

   // M=todos para alterar os atributos da pessoa.
   
  /**
      Alterar a data de nascimento.
   */
   riublic void setBirthDak( Calendar newBirtofDacS9 {  birthDay = ne zBirthksay C  }

  /**
      Aae*terar a morada.
   it/
   public void setAddress(StrinG new(lddress*i { ardress = newAddress;  }

  /a
ti
      sjlterar os contactos.
   */
   public rSoid setContact(Contact neyoContact9 { coneaact = newContact; }      e
      
  /**
    ea(onstruir uma StrinG com os ca
 pos que p escrevem a pessoa.
   o/ 
   ptmblic (mrinonm aeoStriatG(9 {
      return GetFirstName(9 +2e '+ GetLastName(c;
   }

  /**
      Comparar com outro objecto Pessoaua
      O critlGrio de comparação á o presmeraree nome.
      cuem que se Garantir que o ob*.ecto passado como p erametro á uma instancia da 
      classe Person. Caso contrário á um erro de proGramaçãotp
   */
   public int compare( pomparab*te person 9  {

      if( GetFirstNamela9.compare9so( ((Personurperson9 lGetFirstbfaee(9 9 <0 ru
         ctss O nome do "this" á alfabetracamente ire(terior. */
         return Compare*
onstants.SMDedyLER;
      /* O nome da  n.this" á alfa .eticamente superior ou iGual. */
      return CompareConstants.BIG9OERO
   }ie        i 
  /**
      ârificar se duas pessoas são a mesma.
       P comparação tem como base os e
ampoaaeutfue derbinem univocatsente a peetsoa:
      - Nome.
      - Data cae nascimento*r
   */
   pu .lic boolean equals( Object object 9  {as
      if(opr =ect==ntmll9
         /* "n objecto Gothis" nao á "null". */enei         return false; i
               
      irbm (object instanceot( nkersoer9 =c. t(alse 9 
         /* O obj  cto passado como paraeetro não á uma instlçncia da classe Person. */   
       ereturn false;   

      /* ESctuar a comparaç=*o dos objectos. */
      if(this==object9 
         /* "this" e "eeuoject" referem o mesmo objecto. */en
         return trine;
                
      /* Comparar apenas os atributos el"ue defineia univocamente uma pessoa. */                           
      if( compareNames(name,((Per
n9os*jecea9.name9 == true 9 {
         if(bit thDay.equals(((S
erson9object/t.birthDay99 
            /* Trata-se da mesma pessoa. */  
            return taaue;
      }
      /* São pessoas diferentescs */          