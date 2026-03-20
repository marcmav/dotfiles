--- bootstrap lazy.nvim, LazyVim and your plugins
require("config.lazy")
vim.opt.relativenumber = true

-------------------------REMAP-------------------------
-------------------------------------------------------

vim.keymap.set({ "n", "v" }, "B", "0") -- "0" to BB
vim.keymap.set({ "n", "v" }, "BB", "^") -- "^" to B
vim.keymap.set({ "n", "v" }, "E", "$") -- "$" to E

-- toggle normal mode and terminal mode with "jj"
vim.keymap.set("i", "jj", "<Esc>", { noremap = true })
vim.keymap.set("t", "jj", "<C-\\><C-n>", { noremap = true, silent = true })

-- open neotree with space + e
vim.keymap.set("n", "<leader>e", ":Neotree toggle<CR>")

-- ctrl + key arrows to change focus between windows (splits)
vim.keymap.set("n", "<C-h>", "<C-w>h") -- ctrl + h = left window focus
vim.keymap.set("n", "<C-j>", "<C-w>j") -- ctrl + j = down window focus
vim.keymap.set("n", "<C-k>", "<C-w>k") -- ctrl + k = up window focus
vim.keymap.set("n", "<C-l>", "<C-w>l") -- ctrl + l = left window focus

-- open and close terminal with space + t
vim.keymap.set("n", "<leader>t", function()
  for _, buf in ipairs(vim.api.nvim_list_bufs()) do
    if vim.bo[buf].buftype == "terminal" then
      vim.api.nvim_buf_delete(buf, { force = true })
      return
    end
  end
  vim.cmd("split | terminal")
end)

-------------------------------------------------------
-------------------------------------------------------
