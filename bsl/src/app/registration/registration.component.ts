import { Component, ElementRef, ViewChild } from '@angular/core';
import { Route, Router } from '@angular/router';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent {

  constructor(private router: Router){}

  ip_addr:string = "http://127.0.0.1:8000";
  
  registerUser(): void{
    const username:string = (<HTMLInputElement>document.getElementById("username")).value;
    const password:string = (<HTMLInputElement>document.getElementById("password")).value;
    const role:string = (<HTMLInputElement>document.getElementById("role")).value;
    const email:string = (<HTMLInputElement>document.getElementById("email")).value;
    const institution:string = (<HTMLInputElement>document.getElementById("Institution")).value;

    let url = this.ip_addr + "/registration/";
    let data = {
        "username": username,
        "password": password,
        "role": role,
        "email": email,
        "institution": institution
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

  }
}
