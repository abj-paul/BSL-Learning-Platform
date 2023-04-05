import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RegisterComponent } from './register/register.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { OtpVerificationComponent } from './otp-verification/otp-verification.component';
import { TeacherDashboardComponent } from './teacher-dashboard/teacher-dashboard.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { ProfileComponent } from './profile/profile.component';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { InvalidCredentialsComponent } from './login/invalid-credentials/invalid-credentials.component';

@NgModule({
  declarations: [
    AppComponent,
    RegisterComponent,
    OtpVerificationComponent,
    TeacherDashboardComponent,
    HomeComponent,
    LoginComponent,
    ProfileComponent,
    ForgotPasswordComponent,
    InvalidCredentialsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
