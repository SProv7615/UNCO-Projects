import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Fixing What Is Broken';
  query: string;
  deities: any[];

  constructor() {
    this.query = 'Barot';
    this.deities = [
      {
        "name:":"Alteste",
        "title":"The Eldest",
        "description":"Shrouded mostly in mystery, the Eldest is a god of mystery and growth. His chyldren - not the other gods, though they number amongst them! - are the treefolk. And it only to them that he speaks, and only to those who show the most promise, the most personal growth, to whom he deigns to offer any words of wisdom. Often, he will be courteous, of a pleasant mien, even as he offers insight into facets that the treefolk might have failed to consider for themselves.",
        "appearance":"Whenever he appears to those who have gathered his favor, he dredges himself up out of shadows, as shadow. A silhouette, an observer may see glowing eyes, and hazy appendages that very well might be naked branches. Those whom have seen him, when not overwrought with bliss at having met the Eldest, will say that he appears, as his title suggests, sturdy, firm, and yet unwell, as though he were an ancient tree in the midst of winter.",
        "favored children":"Treekin"
      },
      {
        "name": "Helia",
        "title": "The Sanguine Star",
        "description":"",
        "appearance":"",
        "favored children":"Tunnelers",
      },
      {
        "name": "Meesha",
        "title": "The Smith",
        "description":"One half of a whole, The Smith is bound to the Artist",
        "appearance":"",
        "favored children":"Swamp-dwellers",
      }
    ];
  }
}
