// turns nodeList into array - nodeList doesn't have indexOf() method
let navigatorButtons = Array.prototype.slice.call(document.querySelectorAll('.navigator-button'));
let homeNavigatorButton = document.querySelector('.home-navigator');
let bloody_red = '#b50303';

// sections
let headerSection = document.querySelector('header');
let headerSectionDist = headerSection.offsetTop;
let servicesSection = document.querySelector('.services-section');
let servicesSectionDist = servicesSection.offsetTop;
let corpSection = document.querySelector('div.corp-section');
let corpSectionDist = corpSection.offsetTop;
let workSection = document.querySelector('.work-section');
let workSectionDist = workSection.offsetTop;

let sections = [
    {
        name: 'header',
        node: headerSection,
        distance: headerSectionDist
    },
    {
        name: 'services',
        node: servicesSection,
        distance: servicesSectionDist
    },
    {
        name: 'work',
        node: workSection,
        distance: workSectionDist
    },
    {
        name: 'corp',
        node: corpSection,
        distance: corpSectionDist
    },
]

// ----------------------------------SCROLL CODES ----------------------------

activateNavigatorButton(homeNavigatorButton);

navigatorButtons.forEach(button => {
    button.addEventListener('click', () => {
        let section = sectionFromThe(button);
        makeOtherButtonsInactive();
        activateNavigatorButton(button);
        scrollToSection(section);
    })
});

function sectionFromThe(button){
    let buttonIndex = navigatorButtons.indexOf(button);
    return sections[buttonIndex];
}

function scrollToSection(section){
    window.scrollTo({
        top: section.distance,
        left: 0,
        behavior: 'smooth'
    });
}

function makeOtherButtonsInactive(){
    navigatorButtons.forEach(button => {
        inactiveNavigatorButton(button);
    })
}

function activateNavigatorButton(node){
    node.classList.add('active');
}

function inactiveNavigatorButton(node){
    node.classList.remove('active');
}

document.addEventListener('scroll', function(event){
    let scrolledDistance = window.scrollY + window.innerHeight;
    sections.forEach(section => {
        if(scrolledDistance >= section.distance){
            highlightTitleOf(section);
            makeOtherButtonsInactive();
            
            let button = buttonFromTheSection(section);
            activateNavigatorButton(button);
        }
    })
});

function buttonFromTheSection(section){
    let index = sections.indexOf(section);
    return navigatorButtons[index];
}

function highlightTitleOf(section){
    let sectionTitleNode = section.node.querySelector('*').children[0];
    sectionTitleNode.style.transform = 'translate(0,0)';
    sectionTitleNode.style.color = 'white';
    sectionTitleNode.style.filter = 'blur(0)';
}


// ---------------------------------------------------------------------