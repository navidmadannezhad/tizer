// turns nodeList into array - nodeList doesn't have indexOf() method
let navigatorButtons = Array.prototype.slice.call(document.querySelectorAll('.navigator-button'));
let homeNavigatorButton = document.querySelector('.home-navigator');
let bloody_red = '#b50303';

// sections
let aboutSection = document.querySelector('.about-section');
let aboutSectionDist = aboutSection.offsetTop;
let teamSection = document.querySelector('div.team-section');
let teamSectionDist = teamSection.offsetTop;
let workSection = document.querySelector('.work-section');
let workSectionDist = workSection.offsetTop;

let sections = [
    {
        name: 'about',
        node: aboutSection,
        distance: aboutSectionDist
    },
    {
        name: 'team',
        node: teamSection,
        distance: teamSectionDist
    },
    {
        name: 'work',
        node: workSection,
        distance: workSectionDist
    },
]

// ----------------------------------SCROLL CODES ----------------------------

highlightTitleOf(sections[0]);

document.addEventListener('scroll', function(event){
    let scrolledDistance = window.scrollY + window.innerHeight;
    sections.forEach(section => {
        if(scrolledDistance >= section.distance){
            highlightTitleOf(section);
        }
    })
});

function highlightTitleOf(section){
    let sectionTitleNode = section.node.querySelector('*').children[0];
    sectionTitleNode.style.transform = 'translate(0,0)';
    sectionTitleNode.style.color = 'white';
    sectionTitleNode.style.filter = 'blur(0)';
}


// ---------------------------------------------------------------------