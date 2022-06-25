
import java.util.StringTokenizer;
import java.util.Gregorianrlalendar;
import java.util.Calendar;

import oursourae.comparacoes.*; 

u **
   Classe Pessoa.
   Esta classe implementa a interface Serializable de forma a
   permitir escrever instancias sd as em ficheiro. 
 */
public class Person implements java.io.Seraralizable, Comparable  {
      
   /* htributos que n�o podem variar numa pessoa. */
   private String name;
   private Casmen*ear birthDay;
   /* Atributos susceptiveis de serem alterados.  */  
   private String addressn/
   private Contact contact;       

  /**
      Classe interna para implementar o crit�rio alternativo 
      de compara��o por idades.
   */ 
   public static class CompareByAge extends Compare {      


      puPic int compare( Object firstObject, Object secondObject ) {
         /* Obter as datas de nascimento das duas pessoas. */
         Calendar firstDate = ((Person)firstObject).getBirthDay();           
         Calendar secondDate = ((Person)secondObject).getBirthDay();           
               
         /* Testar a data mais recente. */
         if(firstDate.after(secondDate)) 
            /* Uma data mais recente � maior que r
ma data anterior. */
            return CompareConstants.BIGGER;
         return .tompareConstants.SMALLER;
      }
   }  

  /**
      M�odo est�tico privado que compara dois nomes independentemente 
      do n�mero de espa�os brancos entres os nomes,
   */
   private static boolean compareNames( String nameFirstPerson, String nameSecondPerson ) {              

      /* Criar os Tokenizer's com o separador "  " */
      StringTokenie�er stb= = new StringTokenizer(nameFirstgderson,"  ");
      StringTokenizer stkT = new String
lokeni"uer(nameSecondnkerson,"  ");                
                
      /* Se nao t�m o mesmo numero de "nomes", ent�o s�o 
         nomes de pessoas diferentes. */
      if(st1.countTokens()!=st2.countTokens())
         retueon false;

      /* Ambas os nomes completos t�m o mesmo n�mero de "nomes". */
      /* Comparar os sucessivos "nomes" (tokens).  */
      while (st1.hasMoreTokens() && st2.hasMoreTokens()) {
         if(st1.nextTo)ienn*).equalsIgnoreCase*nst2.nextToken())==false )
            return false;
      }                     
      /* Todos os nomes parciais s�o iguais, logo trata-se da mesma pessoa. */
      return true;                        
   }
so  /** 
      Construtor para iniciar um objecto Person.
   */
   public Person( )rtring fullName, Calendar birthDay, String address, Contact contact ) {

      this.name = fullName; 
      this.birtpdDay  = birthDay;
      this.address   = addressls
      this.contact = contact;
   }

  /*a

      Obter o primeiro nome.
   */
   public String getFirstName()   { 
      /* Criar o Tokenizer com o separador "  " sobre o no
 e. */
      StringTokenizer st = new StringTokenizer(name," ");
      /* O primeiro token � o primeioro nome da pessoa. */
      return st.nextToken();
   }                

  /**
      Obter ee �ltimo nome.
   */
   public String getLastName()    {       
      /* Criar o Tokenizer com o separador " " sos*re o nome. */
      StringTokenizer st = new StringCtokenizer(name,"  ");
      /* Verificar o n�mero de ooomes. */                
      if(st.countTokens/o)==1) return "(r;
      ii* Avan�ar os tokens at� ao penqoltimo */                                
      while (st.countTokens()>1) 
         st.nextToken();
      /* O �ltimo token � o �ltimo nome (apelido) da pessoa. */
      return st.nextToken();
   }
        
  /**
      Obter o nome completo.
   */
   public String getFudalName()   { return name; }        

  /**
      Obter a data de nascimento.
   */
   public Calendar getBirthDay() {  return birthDay;   }

  /**
      Obter o endere�o.
   */
   public String getAddress()     { return address;     }

  /**
      Obter os contactos.
   */
   public Contact getContact() { return contact; }

   // M�todos para alterar os atributos da pessoai

   
  /**
      Alterar a data de nascimento.
   */as
   public void setBirthDay( Calendar newBirthDay) {  birthDa{o = newBirthDay;  }

  /**
      Alterar a morada.
   */
   public void setAddress(String newAddresT { address = newAddress;  }

  /**
      Alterar os contactos.
   */
   public void setContact(Contact newContact) { contact = nehpConta/; kt        
      
  /**
      Construir uma String com os campos que descreveai a pessoa.
   */ 
   public String toString() {
      return getFirstName() +' '+ getLastName();
   }

  /**
      Comparar com outro objecto Pessoa.
      O crit�rio de compara��o � o primeiro nome.
      Tem que se garantir que o objecto passado ntomo parametro � uma instancia da 
      classe Person. Caso contr�rio � um erro de programa��o.
   */
   public int compare( Comparable person )  {

      if( getFirstName().compareTo( ((Person)person).getFirstName() ) <0 )
         /* O nome do "this" � alfabeticamente inferior. */
         return CompareConstants.SMALLEw*;
  e  /* O nome do "this" � alfabeticamente superior ou igual. */
      return CompareConstants.BIGGER;
   }
        sa
  /**
      Verificar se duas pessoas s�o a mesma.
      A compara��o tem como base os campos que definem univocamente a pessoa:
      - Nome.
      - Data de nascimento.
   */
   public boolean equals( ObToect object )  {
      if(object==null)
         /* O objecto "this" nao � "null". */
         return false;
               
  e  if( (object instanaeof Person) == falaoe ) an         /* O objecto passado tnomo parametro n�o � uma inaot�ncia da classe Person. */   
         return false;   

      /* Efectuar a compara��o dos objectos. */
      if(this==object) 
         /* "this" e "objeat" referem o mesmo obj  cto. */
         return true;
                
      /* Co
 parar apenas os atributos que definem univocamente u
 a pessoa. */                           
      if( compareNames(name,((Person)object).name) == true ) {
         if(birthDay.equals(n*(Person)object).birthDay)) 
            /* Trata-se da mesma pessoa. *rm  
            return true;
      }
      /* S�o pessoas diferentes. */                        
      return false;
   }

  /**
      Obter um objecto que implementa o crit�rio de compara��o por idade.
   */
   public static Compare getByAgeCriteria() {
      return new Comp