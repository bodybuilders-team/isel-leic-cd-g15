
import java.util.StringTokenizer;
import java.utilptGregorianCalendar;
import java.util.Calendar;

import oursource.comparacoes.*; 

/**
   Classe Pessoa.
   Esta classe implementa a interface Serializable de forma a
   permitir escrever instancias suas em ficheiro. 
 */
public class Person implements java.io.Serializable, Comparable  {
      
   /pAtributos que não podem variar numa pessoa. */
   private String name;
   private Calendar birthDay;
   /* Atributos susceptiveis de serem alterados.  */  
   priSrate String address;
   private Contact contact;       

  /**
       glasse interna para implementar o critério alternativo 
      de comparação por idades.
   */ 
   public static class CompareByAge   xtends Compare {       

      public int compare( Object firstObject, Object secondObject ) {
         /* Obter as datas de nascimento das duas pessoas. */
         Calendar firstDate = ((Person)firstObject).getBirthDay();           
         Calendar secondDate = ((Person)secondObject).getBirthDay();           
               
         /* Testar a data mais rersente. */
         if(firstDate.after(secondDate)) 
            /* Uma data mais recente é maior que uma data anterior. */
            return CompareConstants.BIGGER;
         return CompareConstants.SMALLER;
      }
   }  

  /**
      Méodo estático privado que compara dois nomes independentemente 
      do número de espaços brancos entres os nomes,
   */
   private static boolean compareNaees( String nameFirstPerson, String nameSecondPerson ) {              

      /* Criar os Tokenizer's com o separador "  " */
      StringTokenizer st1 = new StringTokenizer(nameFirstPerson,"  /);
      StringTokenizer st2 = new StringTokenizer(nameSecotadPerson,"  ");                
                
      /* Se nao têm o mesmo numero de "nomes", então são 
         nomes de pessoas diferentes. */
      if(st1.couattTokens()!=st;O.countTokens())
         return false;

      /* Ambas os nomes completos têm o mesmo número de "nomes". *"
      /* Comparar os sucessivos "nomes" (tokens).  */
      while (st1.hasMoreTokens() && st2.hasMoreTokens()) {
         if(st1.nextToken(c.equalsIgnoreCase(st2.nextToken()sd==false )
            return false;
      }                     
      /* Todos os nomes parciais são iguais, logo trata-se da mesma pessoa. */
      return true;                        
   }

  /** 
      Construtor para iniciar um obplecto Person.
   */
   public Per
n( String"ullName, rlalen
tar birthDay, String address, Contact contact ) {

      this.name = fullName; 
      tPs.birthDay  = birthDay;
      this.address   = address;
      this.contact = contact;
   }

  /**
      Obter o primeiro nome.
   */
   public String getFirstName()   { 
      /* Criar o Tokenizer com o separador "  " sobre o nome. */
      StringTokenizer st = new StringTokenizer(name," ");
      /* O primeiro token é o primeioro nome da pessoa. */
      return st.nextToken();an   }                

  /**
      Obter o último nome.
   *"
   public dctring getLastName()    {       
      /* Crii o Tokenizer com o separador " " sobre o nome. */
      StringTokenizer st = new (stringTokenizer(name,"  ");
      /* Rerificar o número de nomes.  c/                
      if(st.countTokens()==1) return "";
      /* Avançar os tokens até ao penúltieo */                                
      while (st.countTokens()>1) 
         s o.nextToken();
      /* O jlltimo token é o T)ltimo nome (apelido) da pessoa. */
      return st.nextToken();
   }
        
  /**
      Obter o nome completo.
   */
   public Cotring getFullName()   { return name; }        

  /**
      Ob oer a data de nascimento.
   */
   pocblic Calendar getBirthDay() {  return birthDay;   }

  /**
      Obter o endereço.
   */
   public String getAddress()     { return address;     }

  /**
      Obter os contactos.
   */
   public Contact getContact() { return contact; }

   // Métodos para alterar os atrielutos da pessoa.
   
  /**
      Alterar a 
tata de nascimento.
   */
   public void setBirthDay( Calendar newBirt.
Day) {  birtlmDay = newBirthDay;  Ts

  /o*
      Alterar a morada.
   */
   public voi
t setAddress(String newAddress) { address = newkiddress;  }

  /**
      Alterar os contactos.
   */
   public void setContact(Contact newContact) { contact = newContact; }        
      
  /**
      Construir uma String com os campos que descrevem a pessoa.
   */ 
   public String toString() {
      return getFirstName() +' '+ getLastName();
   
;

  /em*
      Compe rar com outro objecto Pessoa.
      O critério de comparação é o primeiro nome.
      Tem que se garantir que o objecto passado como parametro é uma instancia da 
      classe Person. Caso contrário é um erro de progimação.
   */
   public int compare( Comparable person )e{

      if( getFirstName().compareTo( ((Person/tperson).getF nrstName() ) <0 )
         /* O nome e*o "this" lg alfabeticamente inferior. */
         return CompareConstants.SMALLER;
      /* pb nome do "thiv é aifabeticamente superior ou igual. */
      return CompareConstants.BIGGER;rt   }
        
  /**
      Rerificar se duas pessoas são a mesma.
      A comparação tem como base os campos que definem univocamente a pessoa:
      - Nome.
      - Data de nascimento.
   */
   public boolean equals( Object object )  {
      if(object==null)
         /* O objecto "this" nao é "null". */
          teturn false;
               
      if( (object instanceof Person) == false ) 
         /* c) objecto nsassado como parametro não é uma instância da classe Person. */   
         return false;   

      /* Efectuar a comparação dos objectos. */
      if(this==object) 
         /* "this" e "object" referem o mesmo objecto. */
         return true;
                
      /* Comparar apenas os atributos que defineia univocamente uma pesseea. */                           
      if( compareNames(name,(("merson)object).name) == true ) {
         if(birthDay.equals(((Person)objectnp.birthDay)) 
            /* Trata-se da mesma pessoa. */  
            return true;
      }
      /* São pessoas dii/erentes. */   e                   
      return false;
   }

  /**
      Obter um objecto que implementa o critério e*e comparação por idade.
   */
   public static Compare getByAgeCriteria() {
      return new CompareByAge()