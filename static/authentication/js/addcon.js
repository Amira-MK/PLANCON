const outers = Array.from(document.getElementsByClassName('outer'));
let active = null;
let queue = Promise.resolve();

const h = document.getElementsByClassName('highlight')[0];
const init = outers[0].style.width;

const u = outers[1].getBoundingClientRect().x - outers[0].getBoundingClientRect().x;

outers.forEach((o,i) => {
	o.dataset.idx = i;
	o.addEventListener('click', ()=>activate(o));
})

function activate(thing){
	if (active === thing) return;
	queue = queue.then(() => {
		return new Promise(r => {
			moveTo(thing);
			minimize(thing).then(()=>expand(thing)).then(r);
			active = thing;
			thing.classList.add('active');
		})
	})
}


function minimize(thing){
	if (!active) return Promise.resolve();
	active.classList.remove('active');
	return new Promise(r => {
		active.addEventListener('transitionend',r,{once:true})
		active.style.width = init;
		h.style.width = init;
	});
}

function moveTo(target){
	h.style.transform = `translateX(${u*target.dataset.idx}px)`
}

function expand(target){
	return new Promise(r => {
		target.addEventListener('transitionend',r,{once: true});
		const width = target.getElementsByClassName('inner')[0].getBoundingClientRect().width + 'px';
		target.style.width = width;
		h.style.width = width;
	})
}

setTimeout(()=>activate(outers[0]),500)

document.querySelectorAll(".drop-zone__input").forEach((inputElement) => {
	const dropZoneElement = inputElement.closest(".drop-zone");
  
	dropZoneElement.addEventListener("click", (e) => {
	  inputElement.click();
	});
  
	inputElement.addEventListener("change", (e) => {
	  if (inputElement.files.length) {
		updateThumbnail(dropZoneElement, inputElement.files[0]);
	  }
	});
  
	dropZoneElement.addEventListener("dragover", (e) => {
	  e.preventDefault();
	  dropZoneElement.classList.add("drop-zone--over");
	});
  
	["dragleave", "dragend"].forEach((type) => {
	  dropZoneElement.addEventListener(type, (e) => {
		dropZoneElement.classList.remove("drop-zone--over");
	  });
	});
  
	dropZoneElement.addEventListener("drop", (e) => {
	  e.preventDefault();
  
	  if (e.dataTransfer.files.length) {
		inputElement.files = e.dataTransfer.files;
		updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
	  }
  
	  dropZoneElement.classList.remove("drop-zone--over");
	});
  });
  
  /**
   * Updates the thumbnail on a drop zone element.
   *
   * @param {HTMLElement} dropZoneElement
   * @param {File} file
   */
  function updateThumbnail(dropZoneElement, file) {
	let thumbnailElement = dropZoneElement.querySelector(".drop-zone__thumb");
  
	// First time - remove the prompt
	if (dropZoneElement.querySelector(".drop-zone__prompt")) {
	  dropZoneElement.querySelector(".drop-zone__prompt").remove();
	}
  
	// First time - there is no thumbnail element, so lets create it
	if (!thumbnailElement) {
	  thumbnailElement = document.createElement("div");
	  thumbnailElement.classList.add("drop-zone__thumb");
	  dropZoneElement.appendChild(thumbnailElement);
	}
  
	thumbnailElement.dataset.label = file.name;
  
	// Show thumbnail for image files
	if (file.type.startsWith("image/")) {
	  const reader = new FileReader();
  
	  reader.readAsDataURL(file);
	  reader.onload = () => {
		thumbnailElement.style.backgroundImage = `url('${reader.result}')`;
	  };
	} else {
	  thumbnailElement.style.backgroundImage = null;
	}
  }