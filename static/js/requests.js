const help = document.querySelector('ul.references li.help')
const modal_layout = document.querySelector('div.modal_layout')
const close = document.querySelector('span.close')
const requests = document.querySelectorAll('ul.requests li div.base_info p.expand')
const requests_info = document.querySelectorAll('ul.requests li div.detail_info')
const attrs = ['0', '0']
show_detail_info = (req) => {
    attrs[0] = req.target.getAttribute('data-id')
    attrs[1] = req.target.getAttribute('data-show')
    requests_info.forEach((request_info) => {
        if (request_info.getAttribute('data-id') === attrs[0]) {
            if (attrs[1] === '0') {
                request_info.style.display = 'flex'
                req.target.setAttribute('data-show', '1')
            } else if (attrs[1] === '1') {
                request_info.style.display = 'none'
                req.target.setAttribute('data-show', '0')
            }
        }
    })
}
requests.forEach((request) => {
    request.addEventListener('click', show_detail_info)
})

show_modal_window_help = () => {
    modal_layout.style.display = 'flex'
    close.addEventListener('click', hidden_modal_window_help)
}
hidden_modal_window_help = () => {
    modal_layout.style.display = 'none'
}
help.addEventListener('click', show_modal_window_help)
