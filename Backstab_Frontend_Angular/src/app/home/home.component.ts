import { Component, OnInit, AfterViewInit  } from '@angular/core';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit, AfterViewInit {
  currentIndex: number = 0;
  prevIndex: number = 0;
  nextIndex: number = 0;
  mouseOver: any = null;
  games: {name: string, discount: string, price: number, price_dc: number, url: string, gameImages: string[]}[] = [
    {name: 'Game 1', discount: '-20%', price: 20, price_dc: 16, url: 'https://cdn.akamai.steamstatic.com/steam/apps/500/header.jpg?t=1682697467', gameImages: ['https://cdn.akamai.steamstatic.com/steam/apps/500/header.jpg?t=1682697467','https://cdn.akamai.steamstatic.com/steam/apps/500/header.jpg?t=1682697467','https://cdn.akamai.steamstatic.com/steam/apps/500/header.jpg?t=1682697467','https://cdn.akamai.steamstatic.com/steam/apps/500/header.jpg?t=1682697467']},
    {name: 'Game 22', discount: '-30%', price: 30, price_dc: 21, url: 'https://cdn.akamai.steamstatic.com/steam/apps/6000/header.jpg?t=1586465290', gameImages: ['https://cdn.akamai.steamstatic.com/steam/apps/6000/header.jpg?t=1586465290','https://cdn.akamai.steamstatic.com/steam/apps/6000/header.jpg?t=1586465290']},
    {name: 'Game 333', discount: '-40%', price: 25, price_dc: 15, url: 'https://cdn.pixabay.com/photo/2023/07/02/18/49/cup-8102791_1280.jpg', gameImages: []},
    {name: 'Game 4444', discount: '-50%', price: 50, price_dc: 25, url: 'https://images.pexels.com/photos/17121023/pexels-photo-17121023/free-photo-of-clouds-over-castle-in-forest.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', gameImages: []},
    {name: 'Game 55555', discount: '-60%', price: 100, price_dc: 40, url: 'https://images.pexels.com/photos/13374672/pexels-photo-13374672.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', gameImages: []},
    {name: 'Game 666666', discount: '-70%', price: 150, price_dc: 45, url: 'https://images.pexels.com/photos/16416071/pexels-photo-16416071/free-photo-of-iced-coffee-and-orange-juice-in-glasses-with-straws.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', gameImages: []}

  ];
  images: string[] = ['https://cdn.akamai.steamstatic.com/steam/apps/500/header.jpg?t=1682697467',
                      'https://cdn.akamai.steamstatic.com/steam/apps/6000/header.jpg?t=1586465290',
                      'https://cdn.pixabay.com/photo/2023/07/02/18/49/cup-8102791_1280.jpg',
                      'https://images.pexels.com/photos/17121023/pexels-photo-17121023/free-photo-of-clouds-over-castle-in-forest.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
                      'https://images.pexels.com/photos/13374672/pexels-photo-13374672.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
                      'https://images.pexels.com/photos/16416071/pexels-photo-16416071/free-photo-of-iced-coffee-and-orange-juice-in-glasses-with-straws.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
                    ];

  constructor() { }

  ngOnInit(): void {
  }

  ngAfterViewInit(): void {
    setInterval(() => {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
      this.updateIndex();
    }, 10000); // Change every 10 seconds
  }

  updateIndex(): void {
    this.prevIndex = (this.currentIndex > 0) 
      ? this.currentIndex - 1 
      : this.images.length - 1;
      
    this.nextIndex = (this.currentIndex < this.images.length - 1) 
      ? this.currentIndex + 1 
      : 0;
  }

  get leftImage() {
    if (this.currentIndex > 0) {
        return this.images[this.currentIndex - 1];
    } else {
        return this.images[this.images.length - 1];
    }
  }

  get centerImage() {
      return this.images[this.currentIndex];
  }

  get rightImage() {
      if (this.currentIndex < this.images.length - 1) {
          return this.images[this.currentIndex + 1];
      } else {
          return this.images[0];
      }
  }
    
  prevImage(): void {
    this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
    this.updateIndex();
  }

  nextImage(): void {
    this.currentIndex = (this.currentIndex + 1) % this.images.length;
    this.updateIndex();
  }

  setCenterImage(image: string): void {
    this.currentIndex = this.images.indexOf(image);
    this.updateIndex();
  }
}
