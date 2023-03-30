import { Component, OnInit } from '@angular/core';
import { LoginCredential } from '../login/login.credential';
import { LoginService } from '../login/login.service';

@Component({
  selector: 'app-edit-user-info',
  templateUrl: './edit-user-info.component.html',
  styleUrls: ['./edit-user-info.component.css']
})
export class EditUserInfoComponent implements OnInit{
  constructor(private loginService: LoginService){}

  selectedEntry : LoginCredential = new LoginCredential();

  ngOnInit(): void {
    this.selectedEntry = this.loginService.getUserList()[0];
  }
  
}
