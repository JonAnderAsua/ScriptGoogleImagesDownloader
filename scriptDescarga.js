// https://www.npmjs.com/package/google-images

//const GoogleImages = require('google-images');
//const client = new GoogleImages('85239165454-1nt7rvm35fuaos9hhkrprkg25j3h6lhr.apps.googleusercontent.com', 'API KEY');
//client.search('Steve Angello')
    //.then(images => {
    //});

//https://www.npmjs.com/package/google-image-downloader

import { ImageDownloader } from '../lib/ImageDownloader';
const downloader = new ImageDownloader(__dirname)
     
downloader.downloadImages('big bang theory', 5)

//https://github.com/dawid-niedzwiecki/google-images-downloader