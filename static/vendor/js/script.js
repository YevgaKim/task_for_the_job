const t_shirts = document.querySelectorAll(".t-shirt"),
        but1 = document.querySelector(".but1"),
        but2 = document.querySelector(".but2");
        
console.log(123123);
show = 0;

function showT_shirt(){
    console.log(show);
    for (let i = 0; i < t_shirts.length; i++){
        if(i==show){
            t_shirts[i].style.display = "block";
        } else{
            t_shirts[i].style.display = "none";
        }
    }
}

showT_shirt();

but1.addEventListener("click", event=>{
    if(show!=0){
        show--;
        showT_shirt();     
    }
});

but2.addEventListener("click", event=>{
    if(show<t_shirts.length-1){
        show++;
        showT_shirt();
    }
});