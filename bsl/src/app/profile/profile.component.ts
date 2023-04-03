import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {
  ip_addr:string = "http://127.0.0.1:8000";
  constructor(private router: Router){}

  logout(): void{
    let myurl = this.ip_addr + "/logout/";
    let data = {
        "authToken": sessionStorage.getItem("authToken"),
        "role": sessionStorage.getItem("role")
    }

    console.log(data);
    fetch(myurl, {
        method: "POST",mode: "cors", cache: "no-cache", credentials: "same-origin", 
        headers: {
        "Content-Type": "application/json",
        },
        redirect: "follow", referrerPolicy: "no-referrer", body: JSON.stringify(data), 
    })
    .then((resolve)=>{
        console.log("Logout Request has been resolved!");
        return resolve.json()
    })
    .then((data)=>{
        console.log("LOGOUT STATUS: "+data.Status);
        sessionStorage.clear();
        this.router.navigate(["login"]);
    })
    .catch((err)=>{
      console.log(err);
    });
  }

  populate_profile(): void{
    const data = {
      authToken: sessionStorage.getItem("authToken"),
      role: sessionStorage.getItem("role")
    };
    
    const queryParams = new URLSearchParams(data.toString()).toString();
    let myurl = this.ip_addr + "/logout/";
    console.log(myurl+"?"+queryParams);

    fetch(myurl + "?" + queryParams, {
      method: "GET",
      mode: "cors",
      cache: "no-cache",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json"
      }
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log("GET request successful:", data);
        document.getElementsByClassName("myRow")[0].innerHTML += data.username;
        document.getElementsByClassName("myRow")[1].innerHTML = data.role;
        document.getElementsByClassName("myRow")[2].innerHTML = data.email;
        document.getElementsByClassName("myRow")[3].innerHTML = data.insitution;

      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
}
