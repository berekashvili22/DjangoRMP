const navSlide = ()=> {
         const burger = document.querySelector('.navbar__burger');
         const nav = document.querySelector('.navbar');
         var body = document.getElementsByTagName('body')[0];
     
         burger.addEventListener('click', ()=>{
             body.classList.toggle('hide-flow');
             nav.classList.toggle('responsive')
             burger.classList.toggle('toggleBurg');
     
     
         });
     }
     
     navSlide();
     
     