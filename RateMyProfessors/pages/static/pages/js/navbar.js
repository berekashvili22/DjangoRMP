const navSlide = ()=> {
         const burger = document.querySelector('.nav__burger');
         const menu = document.querySelector('.menu');
        //  var body = document.getElementsByTagName('body')[0];
     
         burger.addEventListener('click', ()=>{
             console.log('clicked')
             menu.classList.toggle('menu-resp-active')
            //  body.classList.toggle('hide-flow');
            //  nav.classList.toggle('responsive')
             burger.classList.toggle('toggleBurg');
     
     
         });
     }
     
     navSlide();
     
     