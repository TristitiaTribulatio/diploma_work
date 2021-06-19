const create_request = document.querySelector("div.create_request")
const status_of_requests = document.querySelector("div.status_of_requests")
const auth = document.querySelector("div.icon_enter_bg")
const create_request_modal = document.querySelector("form.modal_window_create")
const status_of_requests_modal = document.querySelector("form.modal_window_status")
const auth_modal = document.querySelector("form.modal_window_auth")
const modal_layout = document.querySelector("div.modal_layout")
const close = document.querySelectorAll('span.close')
const forms = document.querySelectorAll('form')
const buttons = [create_request, status_of_requests, auth]

show_modal_window = (button) => {
    let modal = button.target.getAttribute('data-name')
    modal_layout.style.display = 'flex'
    if (modal === "auth") {
        auth_modal.style.display = 'flex'
    } else if (modal === "create") {
        create_request_modal.style.display = 'flex'
    } else if (modal === "status") {
        status_of_requests_modal.style.display = 'flex'
    }
    close.forEach((elem) => {
        elem.addEventListener('click', hidden_modal_window)
    })

}

hidden_modal_window = () => {
    forms.forEach((form) => {
        form.style.display = 'none'
    })
    modal_layout.style.display = 'none'
}

buttons.forEach((elem) => {
    elem.addEventListener('click', show_modal_window)
})






