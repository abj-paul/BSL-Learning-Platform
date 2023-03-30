import { Injectable } from '@angular/core';
import { LoginCredential } from './login.credential';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor() { }

  harcoded_login_credentials : LoginCredential[] = [
    {name:"abhi", password:"stu458"},
    {name:"tashfia", password:"stu458"}
  ];

  saveNewUser(): void{

  }

  authenticate(username: String, password: String): boolean {
    for(let i=0; i<this.harcoded_login_credentials.length; i++){
      if(this.harcoded_login_credentials[i].name == username && this.harcoded_login_credentials[i].password == password) return true;
    }
    return false;
  }

  getUserList(): LoginCredential[]{
    return this.harcoded_login_credentials;
  }
}
