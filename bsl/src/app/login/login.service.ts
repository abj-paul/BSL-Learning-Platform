import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { LoginCredential } from './login.credential';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  ip_addr:string = "http://127.0.0.1:8000";

  constructor(private router: Router) { }

  harcoded_login_credentials : LoginCredential[] = [
    {name:"abhi", password:"stu458"},
    {name:"tashfia", password:"stu458"}
  ];

  saveNewUser(): void{

  }

  authenticate(username: String, password: String): boolean {
    let url = this.ip_addr + "/login/";
    let data = {
        "username": username,
        "password": password,
    }

    console.log(data);
    fetch(url, {
        method: "POST",mode: "cors", cache: "no-cache", credentials: "same-origin", 
        headers: {
        "Content-Type": "application/json",
        },
        redirect: "follow", referrerPolicy: "no-referrer", body: JSON.stringify(data), 
    })
    .then((resolve)=>{
        console.log("Registration Request has been resolved!");
        return resolve.json()
    })
    .then((data)=>{
        console.log("Auth Token: "+data.authToken);
        sessionStorage.setItem("authToken", data.authToken);
        sessionStorage.setItem("role", data.role);
        
        if(data.role=="Teacher") this.router.navigate(['/teacher-dashboard']);
        else if(data.role=="Student") this.router.navigate(['/student-dashboard']);
    })
    .catch((err)=>{
      console.log(err);
    });


    for(let i=0; i<this.harcoded_login_credentials.length; i++){
      if(this.harcoded_login_credentials[i].name == username && this.harcoded_login_credentials[i].password == password) return true;
    }
    return false;
  }

  getUserList(): LoginCredential[]{
    return this.harcoded_login_credentials;
  }
}
