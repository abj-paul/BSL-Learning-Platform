import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'bsl';
  testingServer = ''

  constructor(private http: HttpClient){}

  ngOnInit(): void {
    this._showTestingServerData();
  }

  __getTestingServerData(): Observable<any>{
    return this.http.get<string>('http://127.0.0.1:8000/')
  }

  _showTestingServerData(): void{
    this.__getTestingServerData()
    .subscribe((data:string)=>{
      this.testingServer += data;
    })
  }

}
