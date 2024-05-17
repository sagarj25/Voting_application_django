// const pollItems = document.querySelectorAll('.poll-item-container')
const voteBTN = document.querySelectorAll('.vote-btn')
let pollData = localStorage.getItem('Polls') || '{}'
    pollData = JSON.parse(pollData)
function vote(item){
    if(!!pollData[item])
        pollData[item] = pollData[item] + 1;
    else
        pollData[item] = 1;

    update_poll_data()
}
function update_poll_data(){
    localStorage.setItem('Polls', JSON.stringify(pollData))
    update_progress()
}

voteBTN.forEach(el=>{
    el.addEventListener('click', function(e){
        e.preventDefault()
        var item = el.dataset.item || null
        if(item != null)
            vote(item)
    })
})

function update_progress(){
    var total = 0;
    var items = [];
    Object.entries(pollData).map(item=>{
        items.push(item[0])
        total += parseInt(item[1])
    })
    if(document.getElementById('total-votes') != null)
        document.getElementById('total-votes').innerText = total.toLocaleString('en-US', {style: 'decimal', maximumFractionDigits:2});  
    items.forEach(item => {
        // Skip If the Item does not Exists
        if(document.querySelectorAll(`.poll-item-container[data-item="${item}"]`) == null)
            return;
        var container = document.querySelector(`.poll-item-container[data-item="${item}"]`)

        var percentage = pollData[item] || 0
            percentage = percentage > 0 ? ((percentage / total) * 100) : 0;
            percentage = percentage.toLocaleString('en-US', {style: 'decimal', maximumFractionDigits:2})

        if(container.querySelector('.poll-item-percentage') != null)
            container.querySelector('.poll-item-percentage').innerText = `${percentage}%`

        if(container.querySelector('.poll-item-progress') != null)
            container.querySelector('.poll-item-progress').setAttribute('aria-valuenow', percentage)
        
        if(container.querySelector('.poll-item-progress .progress-bar') != null)
            container.querySelector('.poll-item-progress .progress-bar').style.width = `${percentage}%`
    })
}

window.onload = function(){
    update_progress()
}